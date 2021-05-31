from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag import Tag
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags", methods=['GET'])
def tags():
    tags = tag_repository.select_all()
    return render_template("tags/index.html", tags=tags)

@tags_blueprint.route("/tags", methods=['POST'])
def add_tags():
    tag_name = request.form['tag_name']
    tag_description = request.form['tag_description']
    tag = Tag(tag_name, tag_description)
    tag_repository.save(tag)
    return redirect("/tags")

@tags_blueprint.route("/tags/<id>")
def show_tags(id):
    tag = tag_repository.select(id)
    return render_template("/tags/show.html", tag=tag)

@tags_blueprint.route("/tags/<id>/edit")
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template('tags/edit.html', tag=tag)

@tags_blueprint.route("/tags/<id>", methods=["POST"])
def update_tag(id):
    tag_name = request.form['name']
    tag_description= request.form['desc']
    tag = Tag(tag_name, tag_description, id)
    tag_repository.update(tag)
    return redirect("/tags/"+id)