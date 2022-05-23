#Drew Wiesen - Tackle take home assessment

from github import Github
import json

#Taken from docs to set up an instance of Github
g = Github()

user = g.get_user("drewwiesen155")
repos = user.get_repos()

repo_attrib = [];

#loop that places all audit data into a repo list
for repo in repos:
	temp = {
		"name: ": repo.name,
		"merge commit allowed: ": repo.allow_merge_commit,
		"squash merge allowed: ": repo.allow_squash_merge,
		"rebase merge allowed: ": repo.allow_rebase_merge,
		"auto delete head branch": repo.delete_branch_on_merge
		}
	repo_attrib.append(temp)
	
#print(repo_attrib); for debugging

#finalize as a json file


with open("result.json", "w") as ret_file:
	json.dump(repo_attrib, ret_file)