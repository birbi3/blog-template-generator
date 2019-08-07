#!/usr/bin/env python

from datetime import datetime
import os

def main():
	today = datetime.today().strftime('%b-%d-%Y')
	with open(today+".md", "w") as blog:
		blog.write("# Birb's Nest " + today + "\n")
		blog.write("#### [Home](../index.md)\n")
		blog.write("### All opinions shared here are mine and mine alone\n")
	with open("my-posts.md", "a") as my_posts:
		my_posts.write("\n- [" + today + "] (posts/" + today + ".md)")
	os.system("mv " + today + ".md posts/")

if __name__ == "__main__":
	main()