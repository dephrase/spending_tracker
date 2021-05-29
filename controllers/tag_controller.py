from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag import Tag
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags", methods=['GET'])
def tags():
    tags = tag_repository.select_all()
    return render_template("tags/index.html", tags=tags)

@tags_blueprint.route("/tags", methods=["POST"])
def show_tags():
    tagname = request.form['tag_name']
    tagdesc = request.form['tag_description']
    newtag = Tag(tagname, tagdesc)
    tag_repository.save(newtag)
    return redirect('/tags')

# @tags_blueprint.route("/tags/show")

