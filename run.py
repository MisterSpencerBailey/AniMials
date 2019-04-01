from animials import Animials


def run():
    try:
        animials = Animials()
        sub = animials.random_subreddit()
        image = animials.get_image(sub)
        title = animials.title(image)
        file_type = animials.file_type(image)
        message = animials.create_message(title, file_type)
        animials.send_message(message)
    except AttributeError:
        print('running again')
        run()


run()
