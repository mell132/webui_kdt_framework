import logging

from core.keywords import Keywords
from utils.keywords_utils import kw_step


class AssertKeywords(Keywords):
    # 断言关键字
    @kw_step
    def assert_url(self, step):
        """url断言"""
        expected_url = step["data"]
        actual_url = self.driver.current_url

        assert expected_url in actual_url, f"❌️当前url:{actual_url} 不包含 预期url:{expected_url}"
        logging.info(f"✅️当前url:{actual_url} 包含 预期url:{expected_url}")

        # #捕获异常
        # try:
        #     assert expected_url in actual_url
        #     logging.info(f"✅️当前url:{actual_url} 包含 预期url:{expected_url}")
        # except AssertionError:
        #     logging.error(f"❌️当前url:{actual_url} 不包含 预期url:{expected_url}")

    @kw_step
    def assert_title(self, step):
        """title 断言"""
        expected_title = step["data"]
        actual_title = self.driver.title
        assert expected_title in actual_title, f"❌️当前title:{actual_title} 不包含 预期title:{expected_title}"
        logging.info(f"✅️当前title:{actual_title} 包含 预期title:{expected_title}")

    @kw_step
    def assert_text(self, step):
        """text断言"""
        expected_text = step["data"]
        actual_text = self.find(step).text
        assert expected_text in actual_text, f"❌️当前text:{actual_text} 不包含 预期text:{expected_text}"
        logging.info(f"✅️当前text:{actual_text} 包含 预期text:{expected_text}")

    @kw_step
    def assert_alert_text(self, step):
        expected_text = step["data"]
        actual_text = self.find(step).text
        assert expected_text in actual_text, f"❌️当前text:{actual_text} 不包含 预期text:{expected_text}"
        logging.info(f"✅️当前text:{actual_text} 包含 预期text:{expected_text}")

    @kw_step
    def assert_element_exist(self, step):
        """元素存在断言"""
        element = self.find(step)
        assert element, f"❌️元素不存在{element}"
        logging.info(f"✅️元素存在:{element}")