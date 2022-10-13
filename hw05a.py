import requests
import json


def getUserRepos(userName):       
    API = ("https://api.github.com/users/" + userName + "/repos")
    userData = requests.get(API)
    repositories = json.loads(userData.text)
    userRepos = []
    
    for repository in repositories:
        try:
            userRepos.append(repository.get("name"))
        except:
            userRepos = []
         
    return userRepos

def getCommitnum(userName, repoName):          #  number of commits that are in each of the listed repositories.
    API = "https://api.github.com/repos/" + userName + "/" + repoName + "/commits"
    repoData = requests.get(API)
    commits = json.loads(repoData.text)
    Commitnum = len(commits)

    return Commitnum
        

if __name__ == "_main_":
    userName = input("Enter Github username: ")     
    userRepos = getUserRepos(userName) 
    print("User: " + userName)
    for repository in userRepos:              #Use for Loop to printing name and their commit in associated repos 
        Commitnum = getCommitnum(userName, repository)
        print("Repo: " + repository + " Number of Commits: " + str(Commitnum))