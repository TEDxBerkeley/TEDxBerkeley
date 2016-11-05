.PHONY: deploy staging update

# usage: make deploy m="commit message"
deploy:
	gulp preview
	cd ../tedxberkeley.github.io && \
	git pull --force && \
	cp -r ../TEDxBerkeley/published/* . && \
	cp ../TEDxBerkeley/published/.gitignore . && \
	git add . && \
	git commit -m "deploy: $(m)" --allow-empty && \
	git push

# usage: make staging m="commit message"
staging:
	rm -rf published
	gulp global_json
	gulp preview
	git add .
	git commit -m "stage: $(m)" --allow-empty
	git pull
	git push
	make update

# Pushes the published folder to gh-pages to update the staging webpage.
update:
	git push origin `git subtree split --prefix published master`:gh-pages --force