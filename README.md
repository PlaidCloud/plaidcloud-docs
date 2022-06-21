# The PlaidCloud documentation

This repository contains the assets required to build the [PlaidCloud documentation](https://docs.plaidcloud.com/). We're glad that you want to contribute!

There are also CI and beta versions of the documentation here:
 * [PlaidCloud CI Documentation](https://docs.plaidcloud.io)
 * [PlaidCloud Beta Documentation](https://docs.plaidcloud.net)

## Contributing to the Documentation

There are three main ways to contribute to the documentation depending on how much documentation you plan to develop.
1. Easy (I'm pretending documentation doesn't exist mode) - This is the drive-by approach of simply going to Github and editing a page directly in the web browser.
2. Engaged (I need to work on several pages or restructure things) - You will clone the repo and push commits back and wait for the automatic build to see your contributions.
3. Serious (I plan to contribute significantly) - You will clone the repo and run a local Hugo server to see changes real-time.

## Easy

This requires no cloning or any other local setup for you to contribute to documentation.  Simply go to the [PlaidCloud Documentation Github](https://github.com/PlaidCloud/plaidcloud-docs) repo and navigate
to the page you wish to edit.

Click the `Edit this file` option on the menu and make your edits.

Upon save, the site will be rebuilt and deployed with your latest change.  Since the entire site is rebuilt each time a save is made in this mode, you will need to wait a few minutes before your changes are visible in the IO documentation.

## Engaged

This approach requires very little technical setup other than cloning the [PlaidCloud Documentation Github Repo](https://github.com/PlaidCloud/plaidcloud-docs).

Clone the repo using VS Code's Git repo management area.

Once the repo is cloned locally, it is best to make a new branch from `main` so you can make several changes before committing them and triggering the rebuild process.  Once you have your changes completed,
commit and push them.  Open a pull request to merge them into `main` from your branch.

Once your PR is accepted and your changes merge into `main` then the IO site will be rebuilt within a few minutes.

## Serious

This is very much like the **Engaged** approach but with the ability to see your changes live by running a local Hugo server.

Again, the need to run the Hugo server locally will boost productivity if you are contributing many changes but is likely not necessary for quick changes and additions that follow standard markdown conventions.

### Using this repository

You can run the website locally using Hugo (Extended version), or you can run it in a container runtime. For web deployments, we strongly recommend using the container runtime, as it gives deployment consistency with the live website.
However, for documentation development locally, the live local server is fast and efficient.

### Prerequisites

To use this repository, you need the following installed locally:

- [npm](https://www.npmjs.com/)
- [Go](https://golang.org/)
- [Hugo (Extended version)](https://gohugo.io/)

#### Windows-specific instructions
It is highly recommended that you take the time to follow the setup of a local Window dev machine.  This will cover necessary setup of, git, ssh keys and an IDE.  Install VS Code at a minimum.
[Window Dev Environment runbook](https://docs.google.com/document/d/1E7tNj4_-6gEP735n9wzLs84yyfdgd6LSi-VwRDJ4fuM/edit#heading=h.noa01ern07k7)

Before you start, install the dependencies. Clone the repository and navigate to the directory:
##### npm
[nodejs.org/en/download](nodejs.org/en/download)
Get the LTS version.
Run the wizard.

##### go
[go.dev/dl](go.dev/dl)
Download and install.

##### hugo
[https://github.com/gohugoio/hugo/releases/](https://github.com/gohugoio/hugo/releases/)
- Go to top (latest) release. (v0.101 as of this writing).
- Locate the hugo **extended** zip file for Windows 64 bit.  It will look about like this: *hugo_extended_0.101.0_Windows-64bit.zip*

- Create a directory **Hugo** on your local C drive.
- Create a subdirectory **bin** inside of **Hugo**
- Unzip the hugo_extended_0.101.0_Windows-64bit.zip file to **C:\Hugo\bin**
- Add C:\Hugo\bin to Windows system paths.  Go [here](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/) for help on this.
- Open Windows command prompt.
- Type this:
```bash
hugo --help
```
This output should show available hugo commands.  If it did not, then the hugo installation is not complete, or the path variable is not correct.

#### Linux

##### npm
```bash
sudo apt install npm
```
##### go
```bash
sudo apt update
sudo apt search golang-go
sudo apt install golang-go
```
##### hugo
[https://computingforgeeks.com/how-to-install-hugo-on-ubuntu-debian/](https://computingforgeeks.com/how-to-install-hugo-on-ubuntu-debian/)
```bash
sudo apt update
	sudo apt -y install hugo
```


```bash
git clone https://github.com/PlaidCloud/plaidcloud-docs.git
cd plaidcloud-docs
```

The PlaidCloud website uses the [Docsy Hugo theme](https://github.com/google/docsy#readme). Even if you plan to run the website in a container, we strongly recommend pulling in the submodule and other development dependencies by running the following:

```bash
# pull in the Docsy submodule
git submodule update --init --recursive --depth 1
```

### Running the website locally using Hugo

To build and test the site locally, run:

```bash
# install dependencies
npm ci
make serve
```

If you get an error complaining about package-lock.json, then try the following:
```bash
# install dependencies
npm install
npm ci
make serve
```
### Running Hugo
Using a console, navigate to ```C:\Users\<your_user>\src\plaidcloud_docs```

Run this:
```bash
hugo serve -D --panicOnWarning
```

This will start the local Hugo server on port 1313. Open up your browser to <http://localhost:1313> to view the website. As you make changes to the source files, Hugo updates the website and forces a browser refresh.

Keep in mind that the local server is not recreating all the static content so changes to templates might require a restart of the local hugo server for the template changes to be incorporated in what you see.

### Orientation
##### Rendered view:
<http://localhost:1313/tips/test/> corresponds to the following:
- <https://docs.plaidcloud.io/tips/test/> on the continuous integration site.
- <https://docs.plaidcloud.com/tips/test/> on the beta site.
- <https://docs.plaidcloud.com/tips/test/> on the production site.

##### Source View
```<https://raw.githubusercontent.com/PlaidCloud/plaidcloud-docs/main/content/en/tips/test.md>```

##### Local Source View
```C:\Users\<your_user>\src\PlaidCloud/plaidcloud-docs/main/content/en/tips/test.md>```

##### Making a change 
Make a change to an .md file will automatically cause change to be available within the local http://localhost:1313/ site.

Commit the change and push to the **main** branch of the **plaidcloud-docs** repo, and it will appear at <https://docs.plaidcloud.io> within 1 hour.

### Key Points
- Avoid unnecessary use of screenshots.  They go stale quickly.
- Structure of repo is important.
- Don’t forget the _index.md files in each folder.
- You can set menu priority by weight in frontmatter on _index.md
- Use includes for common sections among pages.
- Reference the example template to see syntax and advanced usage options .
- When you push to main, the docs.plaidcloud.io site is built and deployed automatically.
- Beta (.net) and Production (.com) are built and deployed by pushing (PR Merge) to respective branches.
- Always use relative links to pages so they operate correctly within each environment.
- Multi-language support is built-in but we only have English now.
- Always start with heading 2 (## Heading 2), never heading 1 since that is automatically added as page title.
- Copy and paste.  Start a new page by copying from the template or another page.
- VSCode has several extensions for managing markdown files.



### Troubleshooting

#### error: failed to transform resource: TOCSS: failed to transform "scss/main.scss" (text/x-scss): this feature is not available in your current Hugo version

Hugo is shipped in two set of binaries for technical reasons. The current website runs based on the **Hugo Extended** version only. In the [release page](https://github.com/gohugoio/hugo/releases) look for archives with `extended` in the name. To confirm, run `hugo version` and look for the word `extended`.

#### Troubleshooting macOS for too many open files

If you run `make serve` on macOS and receive the following error:

```bash
ERROR 2020/08/01 19:09:18 Error: listen tcp 127.0.0.1:1313: socket: too many open files
make: *** [serve] Error 1
```

Try checking the current limit for open files:

`launchctl limit maxfiles`

Then run the following commands (adapted from <https://gist.github.com/tombigel/d503800a282fcadbee14b537735d202c>):

```shell
#!/bin/sh

# These are the original gist links, linking to my gists now.
# curl -O https://gist.githubusercontent.com/a2ikm/761c2ab02b7b3935679e55af5d81786a/raw/ab644cb92f216c019a2f032bbf25e258b01d87f9/limit.maxfiles.plist
# curl -O https://gist.githubusercontent.com/a2ikm/761c2ab02b7b3935679e55af5d81786a/raw/ab644cb92f216c019a2f032bbf25e258b01d87f9/limit.maxproc.plist

curl -O https://gist.githubusercontent.com/tombigel/d503800a282fcadbee14b537735d202c/raw/ed73cacf82906fdde59976a0c8248cce8b44f906/limit.maxfiles.plist
curl -O https://gist.githubusercontent.com/tombigel/d503800a282fcadbee14b537735d202c/raw/ed73cacf82906fdde59976a0c8248cce8b44f906/limit.maxproc.plist

sudo mv limit.maxfiles.plist /Library/LaunchDaemons
sudo mv limit.maxproc.plist /Library/LaunchDaemons

sudo chown root:wheel /Library/LaunchDaemons/limit.maxfiles.plist
sudo chown root:wheel /Library/LaunchDaemons/limit.maxproc.plist

sudo launchctl load -w /Library/LaunchDaemons/limit.maxfiles.plist
```

This works for Catalina as well as Mojave macOS.

## Thank you for your Help!

PlaidCloud documentation is important because it helps our user community, allows people to be self-sufficient, and provides a positive feedback loop for prospective community members to feel they have the information necessary to get started.
