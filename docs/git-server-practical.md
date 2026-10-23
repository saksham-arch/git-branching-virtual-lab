# Git server and hosted remote practical — Unit 1.3

## Local server model

Run this exercise in a new disposable directory. A bare repository represents the remote server; two clones represent two students. Set your own Git author identity if not already configured.

```bash
mkdir git-server-practice
cd git-server-practice
git init --bare classroom.git
git clone classroom.git student-a
cd student-a
git switch -c main
printf 'Initial record\n' > record.txt
git add record.txt
git commit -m 'Add initial record'
git push -u origin main
cd ..
git clone -b main classroom.git student-b
cd student-b
git switch -c observations
printf 'Second observation\n' >> record.txt
git commit -am 'Add observation'
git push -u origin observations
cd ../student-a
git fetch origin
git merge origin/observations
git push origin main
git log --graph --oneline --all
```

Observe that fetch updates remote-tracking references without changing the current working tree. Merge integrates the chosen history. To reproduce a conflict, edit the same original line differently in both clones, commit and push from one, then fetch and merge in the other. Resolve the conflict markers, stage the file and commit. The original web experiment at `/` provides a guided equivalent, but its terminal is a simulation.

## Hosted server (GitHub)

Create an empty repository in your own account with the intended visibility. Do not copy tokens into source files or terminal examples. Use the account's normal SSH-key or credential-manager workflow. Substitute the actual clone URL from GitHub:

```bash
git remote add hosted git@github.com:YOUR-ACCOUNT/YOUR-PRACTICE-REPOSITORY.git
git push -u hosted main
git push hosted origin/observations:refs/heads/observations
```

Open a pull request for the observations branch, inspect its diff, and merge it using your repository's review policy. Then `git fetch hosted` and inspect the remote-tracking history. Do not push the course's private student data or databases.

## SSH Git server implementation

On a Linux machine you administer, install Git and SSH through the operating system package manager. Create a dedicated Git account, install only authorized students' public SSH keys, and restrict that account to `git-shell`. Example repository initialization by the server administrator:

```bash
sudo adduser --disabled-password --gecos '' git
sudo chsh -s /usr/bin/git-shell git
sudo mkdir -p /srv/git/classroom.git
sudo git init --bare /srv/git/classroom.git
sudo chown -R git:git /srv/git/classroom.git
```

The administrator must create `/home/git/.ssh/authorized_keys` with directory mode 700, file mode 600 and ownership `git:git`. Add verified **public** keys, never private keys. Verify the SSH host fingerprint through a trusted channel. A client then uses:

```bash
git remote add classroom git@YOUR-SERVER:/srv/git/classroom.git
git push -u classroom main
```

Record access denied for an unauthorized key, successful access for an authorized key, and a restored repository from a backup. Shared write access requires branch protection or server-side receive hooks, logging and regular backups; a bare repository by itself is not a complete permission policy. These commands are a deployment procedure, not a claim that an external SSH server has been provisioned.

Reference: [Pro Git — Setting Up the Server](https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server).
