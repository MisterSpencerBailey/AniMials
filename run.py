from animials import Animials


def run():
    try:
        animials = Animials()
        sub = animials.random_subreddit()
        image = animials.get_image(sub)
        title = animials.title(image)
        message = animials.create_message(title)
        animials.send_message(message)
    except AttributeError:
        print('running again')
        run()


run()
