from instabot import Bot
import json
import os
from config import Config
from app import db
from app.models import Posts
import schedule


def main():

    def check_inst_activity():
            bot = Bot()
            username = Config.INST_USERNAME
            password = Config.INST_PASSWORD
            bot.login(username=username, password=password)
            user_id = bot.get_user_id_from_username(username)
            twony_last_medias = bot.get_user_medias(user_id, filtration=None)
            with open('posts_info.json') as info_file:
                posts_json = json.load(info_file)

                current_posts = {
                    'posts': []
                }
                for i in twony_last_medias:
                    if i not in posts_json['posts']:
                        post_info = bot.get_media_info(i)[0]
                        post = Posts()
                        post.post_id = i
                        post.text = post_info['caption']['text']
                        if post_info['media_type'] == 1:
                            post.photo_path = post_info['image_versions2']['candidates'][0]['url']
                        elif post_info['media_type'] == 8:
                            post.photo_path = post_info['carousel_media'][0]['image_versions2']['candidates'][0]['url']
                        else:
                            continue
                        db.session.add(post)
                    current_posts['posts'].append(i)
                for i in Posts.query.all():
                    if i.post_id not in twony_last_medias:
                        db.session.delete(i)
                db.session.commit()
            with open('posts_info.json', 'w') as posts_info_json:
                json.dump(current_posts, posts_info_json)
            os.remove(f'config/{username}.checkpoint')
            os.remove(f'config/{username}_uuid_and_cookie.json')
    check_inst_activity()
    # schedule.every(3).day.do(check_inst_activity)
    #
    # while True:
    #     schedule.run_pending()

main()


