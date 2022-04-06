# NOTE: Generated By HttpRunner v3.1.8
# FROM: .\har\index.har
# -*- coding: big5 -*-

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseIndex(HttpRunner):

    config = Config("搜索框热词").verify(False)

    teststeps = [
        Step(
            RunRequest("/module/searchtags")
            .get("https://office.safe.360.cn/module/searchtags")
            .with_params(
                **{
                    "inst_type": "0",
                    "m2": "bdac9c5161c743c2f280cadf3398e35272963b712974",
                    "mid": "545623be9cff9c7c1486c09dbc9b28a3",
                    "q": "mTJx2OTVQbcacf925+s/Mz8gnPjBlRSUuMZUNSI2SZ5urh30hCkGDKVrF0LCzbL/zPwrtuSoN4THBTXrDF184MBvCI06rqfO7dMrkW/bjsL1qz1xDzvyBPrhSUtDVzz4haTn6HlK0FTARsHw3OW7pz3vDV/KB2SMsinxLJC9OmQ=",
                    "rand": "129977",
                    "secore_inst_type": "3",
                    "secore_ver": "13.1.5270.0",
                    "sign": "7b793723f162777d0f0a3a7bc649c17d",
                    "timestamp": "1649234736",
                    "version": "2.0.0.1231",
                }
            )
            .with_headers(
                **{
                    "Host": "office.safe.360.cn",
                    "Accept": "*/*",
                    "Cookie": "Q=u%3DYYNO..%26n%3Dnnyyoo__%26le%3D%26m%3DZGpmWGWOWGWOWGWOWGWOWGWOZwN5%26qid%3D3286970398%26im%3D1_t0168deca91e10180f2%26src%3Dpcw_guard_safe_weixin%26t%3D5;T=s%3D8139957378a18568e8bfad35141fabe1%26t%3D1648547505%26lm%3D%26lf%3D%26sk%3Dae9bf01b94828e0dab69423fb17a09ba%26mt%3D1648547505%26rc%3D%26v%3D2.0%26a%3D1;S=",
                }
            )
            .with_cookies(
                **{
                    "Q": "u%3DYYNO..%26n%3Dnnyyoo__%26le%3D%26m%3DZGpmWGWOWGWOWGWOWGWOWGWOZwN5%26qid%3D3286970398%26im%3D1_t0168deca91e10180f2%26src%3Dpcw_guard_safe_weixin%26t%3D5",
                    "T": "s%3D8139957378a18568e8bfad35141fabe1%26t%3D1648547505%26lm%3D%26lf%3D%26sk%3Dae9bf01b94828e0dab69423fb17a09ba%26mt%3D1648547505%26rc%3D%26v%3D2.0%26a%3D1",
                    "S": "",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json; charset=utf-8")
            .assert_equal("body.errno", 0)
            .assert_equal("body.errmsg", "")
            .assert_equal("body.type", 0)
            .assert_equal("body.t_str", "")
            .assert_equal("body.data.list[0]", "万圣节")
            .assert_equal("body.data.list[1]", "春节")
            .assert_equal("body.data.list[2]", "劳动节")
            .assert_equal("body.data.list[3]", "中秋节")
            .assert_equal("body.data.list[4]", "元旦节")
            .assert_equal("body.data.list[5]", "简历")
            .assert_equal("body.data.list[6]", "圣诞节")
            .assert_equal("body.data.list[7]", "总结汇报")
        )
    ]
