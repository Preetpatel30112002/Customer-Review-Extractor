from playwright.sync_api import sync_playwright
from llm_helper import get_likely_review_elements
import time

def extract_review_data(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        try:
            page.goto(url)
            page.wait_for_load_state("networkidle")

            html_content = page.content()
            selector = get_likely_review_elements(html_content)
            print("LLM Suggested Selector:", selector)

            if not selector or not selector.strip():
                print("Selector could not be retrieved. Exiting extraction.")
                return []

            all_reviews = []

            while True:
                reviews_elements = page.query_selector_all(selector)
                if not reviews_elements:
                    print("No reviews found with the current selector.")
                    break

                for review_element in reviews_elements:
                    try:
                        reviewer = review_element.query_selector(".reviewer") or review_element.query_selector(".author")
                        rating_element = review_element.query_selector('[data-rating]')
                        title = review_element.query_selector(".title") or review_element.query_selector("h3")
                        body = review_element.query_selector(".review-body") or review_element.query_selector(".description")

                        all_reviews.append({
                            "reviewer": reviewer.inner_text() if reviewer else None,
                            "rating": rating_element.get_attribute("data-rating") if rating_element else None,
                            "title": title.inner_text() if title else None,
                            "body": body.inner_text() if body else None,
                        })
                    except Exception as e:
                        print(f"Error extracting single review: {e}")

                try:
                    load_more_button = page.locator(".load-more")
                    if load_more_button.is_visible():
                        load_more_button.click()
                        time.sleep(2)
                        page.wait_for_load_state("networkidle")
                    else:
                        next_page_button = page.locator(".next-page")
                        if next_page_button.is_visible():
                            next_page_button.click()
                            time.sleep(2)
                            page.wait_for_load_state("networkidle")
                        else:
                            break
                except Exception as e:
                    print(f"Pagination error: {e}")
                    break

            return all_reviews

        except Exception as e:
            print(f"Error: {e}")
            return []

        finally:
            context.close()
            browser.close()
