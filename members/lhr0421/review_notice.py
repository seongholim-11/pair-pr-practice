"""Generate a short pull-request review notice."""

import argparse


def build_review_notice(author: str, title: str, url: str) -> str:
	"""Build a review request message from pull-request details."""
	return f"리뷰 부탁드립니다: {title} ({author})\n{url}"


def main() -> None:
	parser = argparse.ArgumentParser(description="리뷰 요청 공지를 생성합니다.....")
	parser.add_argument("author", help="PR 작성자")
	parser.add_argument("title", help="PR 제목")
	parser.add_argument("url", help="PR 주소")
	args = parser.parse_args()
	print(build_review_notice(args.author, args.title, args.url))


if __name__ == "__main__":
	main()
