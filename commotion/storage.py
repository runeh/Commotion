from os import listdir
from os.path import join, getctime, getmtime, isdir, isfile, basename, abspath

def load_storage(path):
    """Figures out what path is, should be uri i guess, and returns an
    instance"""
    return FileStystemBlogStorage(path)


class BlogStorageError(Exception):
    pass


class BlogStorage(object):
    def posts(self):
        """Return all posts, sorted by newnes"""
        raise NotImplemented

    def post_for_slug(self, slug):
        raise NotImplemented

    def options(self):
        """Return a dict of options for the blog site"""    
        raise NotImplemented


    def _guess_post_format(self, path):
        """Try to figure out the post format based on either file name,
        content or other heuristics. For now it's ALEWAYS MARKDOWN"""
        return "markdown"


class FileStystemBlogStorage(BlogStorage):
    """Dumb test storage backend that just uses a directory with no meta
    data.

    Note: ctime does't show created time on all OSes, thus touching will
    change pubdate of stuff. User name doesn't work without using
    silly stuff with stat and the pwd module.

    A git backend should be able to derive from this and overide
    _get_post_meta to use info from git.

    Assume posts are stored in ./posts/<dirname>/index.markdown
    """
    def __init__(self, path):
        if not isdir(path):
            raise BlogStorageError("Blog root directory not found")

        self.root = abspath(path)

    def posts(self):
        postsdir = join(self.root, "posts")
        if not isdir(postsdir):
            return []
        
        posts = []
        for directory in [join(postsdir, e) for e in listdir(postsdir)]:
            post = self._load_post(directory)
            if post:
                posts.append(post)
        return sorted(posts, key=lambda e: e["ctime"])

    def post_for_slug(self, slug):
        path = join(self.root, "posts", slug)
        return self._load_post(path)

    def _load_post(self, path):
        """Parse a single post dir/file"""
        postfile = join(path, "index.markdown")
        draftmarker = join(path, "DRAFT")
        if not isdir(path) or not isfile(postfile) or isfile(draftmarker):
            return None

        post = {}
        post["ctime"] = getctime(path)
        post["mtime"] = getmtime(path)
        post["author_name"] = "unknown"
        post["format"] = self._guess_post_format(postfile)
        post["path"] = join("post", basename(path)) + "/"
        post["mediapath"] = join(self.root, "posts", basename(path)) + "/"
        post["title"] = basename(path).replace("_", " ").title()
        post["content"] = open(postfile).read()
        post.update(self._get_post_meta(path))
        return post

    def _get_post_meta(self, path):
        """Should load post.ini, or something similar, that can override
        all the other metadata, like publish time, author, slug/title"""
        return {}

