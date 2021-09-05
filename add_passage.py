import time


def main():
    account, link, date_time, header, content = passage_input()
    passage_html = html_formatter(account, link, date_time, header, content)
    insert_html(passage_html)


def insert_html(html: str):
    # INSERT THE HTML CODE INTO THE EXISTING FILES
    # APPEND TO PASSAGE.HTML
    existing_passage_html = open('./test_files/passages.html', "r+")
    existing_passage_html_lines = existing_passage_html.readlines()
    # TURN HTML CODE INTO A LIST
    html_list = html.splitlines(True)
    # INSERT
    index = 36  # start at line 36, should be changed once html file change
    for _ in html_list:
        existing_passage_html_lines.insert(index, _)
        index += 1
    existing_passage_html.writelines(existing_passage_html_lines)
    existing_passage_html.close()


def html_formatter(account, link, date_time, header, content):
    # TURN PASSAGE INTO HTML CODE
    # DETAIL
    passage_detail = '<h5 class="passage detail"><a href="%s" target="_blank">%s</a>　︎%s</h5>' % (
        link, account, date_time
    )
    # HEADER
    passage_header = '<h3 class="passage header">%s</h3>' % header
    # CONTENT
    passage_content = '<small class="passage content">%s</small>' % content
    # FINAL HTML CODE
    passage_html = """
<p>
                %s
                %s
                %s
            </p>
""" % (passage_detail, passage_header, passage_content)
    return passage_html


def passage_input():
    # INPUT PASSAGE AND
    def datetime():
        # FORMAT DATE AND TIME
        year, mon, day, hour, min = tuple(time.localtime())[0], tuple(time.localtime())[1], tuple(time.localtime())[2], \
                                    tuple(time.localtime())[3], tuple(time.localtime())[4]
        date_time = "%d年%d月%d日%d:%d" % (year, mon, day, hour, min)
        # print(date_time)
        return date_time

    def account_link(passage_account: int):
        # FIND THE CORRECT LINK AND ACCOUNT
        account_link_dict = {"rrestlesS": "https://t.me/rrrrrestlesssss"}
        account_link_dict_index = [key for key, value in account_link_dict.items()]
        account = account_link_dict_index[passage_account]
        link = account_link_dict[account]
        return account, link

    # DETAIL
    account_info = """
Telegram: 0
Select your account: """
    while True:
        try:
            account_selection = input(account_info)
            account, link = account_link(int(account_selection))
            break
        except:
            print("Index Not Found")
            pass
    date_time = datetime()
    # print(passage_detail)
    # HEADER
    header = input("HEADER: ")
    # CONTENT
    stop_word = ':q'  # input to stop
    content = ''
    for line in iter(input, stop_word):
        content += line + '\n'
    return account, link, date_time, header, content


if __name__ == '__main__':
    main()
