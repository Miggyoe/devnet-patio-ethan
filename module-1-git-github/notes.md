# Module 1 — Git & GitHub

**Student:** Ethan Miguel P. Patio
**Date:** September 27, 2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

Git is the version control that runs on the local computer while Github is the cloud where you store your codes through internet.
---

## Key vocabulary (in your own words)

- repository: this is where you store your projects like a folder that contains your files, history and more. 
- commit: the snapshot of the changes you made to the repository with commit message.
- branch: a different folder or a place you working on without affecting the main branch
- push / pull: push uploads the changes you made, while pull downloads the updated changes into you local repository
- pull request: this is a request to check the submitted changes by a contributor to merge their branch to the main branch
- merge conflict: an error when Git can't merge changes

---

## Walking through what I did

[Describe, step by step, a real branch → commit → push → PR you did. Include the actual commands you used.]
First, I made my own branch "notes" and make some changes. I want to stage my specific file "notes.md" and save it using git commit command with a message "answered the walking through what I did part". Lastly, I uploaded the changes using the git push command

```
# paste your actual commands here
git switch -c "notes"
git add module-1-git-github/notes.md
git commit -m "answered the walking through what I did part"
git push -u origin "notes"
```

---

## A mistake I made (or one I want to avoid)

[What tripped you up? A confusing error message, committing to the wrong branch, a merge conflict — explain it so a classmate reading this avoids the same mistake.]

---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]
