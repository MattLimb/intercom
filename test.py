import gitlab

gi = gitlab.Gitlab("https://gitlab.com/")

print(gi.projects.get(10582521).name)
print(gi.projects.get(10582521).web_url)


print(gi.projects.get(10582521).releases.list(sort="desc")[0].tag_name)