#! /usr/bin/env python

import argparse
import time
import getpass

import tools.wall as wall

from seleniumrequests import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

MAX_POSTS = 5000
SELENIUM_EXCEPTIONS = (NoSuchElementException, StaleElementReferenceException)

def run_delete():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-E",
        "--email",
        required=True,
        dest="email",
        type=str,
        help="Your email address associated with the account"
    )

    parser.add_argument(
        "-P",
        "--password",
        required=False,
        dest="password",
        type=str,
        help="Your Facebook password"
    )

    parser.add_argument(
        "-U",
        "--profile-url",
        required=True,
        dest="profile_url",
        type=str,
        help="The link to your Facebook profile, e.g. https://www.facebook.com/your.name"
    )

    parser.add_argument(
        "-H",
        "--headless",
        action="store_true",
        dest="is_headless",
        default=False,
        help="Run browser in headless mode (no gui)"
    )

    args = parser.parse_args()

    args_user_password = args.password or getpass.getpass('Enter your password: ')

    wall.delete_posts(
            user_email_address=args.email,
            user_password=args_user_password,
            user_profile_url=args.profile_url,
            is_headless=args.is_headless
    )

if __name__ == "__main__":
    run_delete()
