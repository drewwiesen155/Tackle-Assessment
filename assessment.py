#Drew Wiesen - Tackle take home assessment

from github import Github

#Taken from docs to set up an instance of Github
g = Github("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")

user = g.get_user("drewwiesen155")
repos = user.get_repos()

repo_attrib = [];

for repo in repos:
    repo_attrib.append([repo.allow_merge_commit, repo.allow_squash_merge, repo.allow_rebase_merge])
	
#print(repo_attrib);