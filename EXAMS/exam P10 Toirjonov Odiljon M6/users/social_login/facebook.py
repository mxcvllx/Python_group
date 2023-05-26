import facebook


class Facebook:

    @staticmethod
    def validate(auth_token):

        try:
            graph = facebook.GraphAPI(access_token=auth_token)
            profile = graph.request('/me?fields=name,email')
            return profile
        except:  # noqa
            return "The token is invalid or expired."
