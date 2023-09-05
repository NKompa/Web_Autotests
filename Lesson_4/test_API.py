import requests
import logging
import yaml

with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
    address = testdata['address_posts_API']
    other_post_title = testdata['other_post_title_API']
    my_title = testdata['my_post_title_API']
    my_description = testdata['my_post_description_API']
    my_content = testdata['my_post_content_API']

S = requests.Session()


def get_other_posts(token):
    response = S.get(url=address, headers={"X-Auth-Token": token}, params={'owner': 'notMe'})
    if response:
        posts_titles = [i['title'] for i in response.json()['data']]
        logging.debug('Got other posts titles.')
        return posts_titles
    else:
        logging.error("Other posts are not available.")


def get_my_posts(token):
    response = S.get(url=address, headers={"X-Auth-Token": token})
    if response:
        posts_descriptions = [i['description'] for i in response.json()['data']]
        logging.debug('Got my posts descriptions.')
        return posts_descriptions
    else:
        logging.error("My posts are not available.")


def publish_post(token):
    post_data = {
        'title': my_title,
        'description': my_description,
        'content': my_content
    }
    response = S.post(url=address, headers={"X-Auth-Token": token}, json=post_data)
    if response:
        logging.debug('Created a new post')
        return response.json()
    else:
        logging.error('Cannot create a post')


def test_other_posts_api(get_api_token):
    assert other_post_title in get_other_posts(get_api_token)


def test_my_posts_api(get_api_token):
    publish_post(get_api_token)
    assert my_description in get_my_posts(get_api_token)
