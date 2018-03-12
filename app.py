# -*- coding: utf-8 -*-
from flask import Flask, render_template, request,Markup
from PortScanner import *
import random

app=Flask(__name__)


@app.route('/',methods=['get','post'])
@app.route('/portscan', methods=['get', 'post'])
def port_scan():
    if request.method == 'POST':
        try:
            host = request.form.get("host")
            ports=request.form.get('ports')
            threads=request.form.get('threads')

            if host:
                if not ports:
                    templates = "<div class=\"alert alert-danger error\" role=\"alert\">Port有误</div>"
                    return render_template("index.html", data=Markup(templates))
                try:
                    templates = "<table id=\"table\" style=\"overflow-y: auto\"><thead><tr><th>Host</th><th>Port</th><th>Service name</th><th>Banner</th></tr></thead><tbody>"
                    dict_res=start(host=host,ports=ports)
                    for i in dict_res:
                        for s in range(len(list(i.values())[0])):
                            if s == 0:
                                add_table = """
                                               <tr>
                                                    <td>%s</td>
                                                    <td>%s</td>
                                                    <td>%s</td>
                                                    <td>%s</td>
                                               </tr>
                                            """ % (list(i.keys())[0], list(i.values())[0][s][0], list(i.values())[0][s][1], list(i.values())[0][s][2])
                            else:
                                add_table = """
                                               <tr>
                                                    <td>%s</td>
                                                    <td>%s</td>
                                                    <td>%s</td>
                                                    <td>%s</td>
                                               </tr>
                                            """ % (" ", list(i.values())[0][s][0], list(i.values())[0][s][1], list(i.values())[0][s][2])
                            templates += add_table
                    templates += "</tbody></table><script src=\"/reload\"></script>"
                    clear_progress()
                    print(dict_res)
                    return render_template('index.html', data=Markup(templates))
                except:
                    templates = "<div class=\"alert alert-danger error\" role=\"alert\">网络错误</div>"
                    return render_template('index.html',data=Markup(templates))
            else:
                templates = "<div class=\"alert alert-danger error\" role=\"alert\">host有误</div>"
                return render_template("index.html", data=Markup(templates))
        except:
            pass
    else:
        return render_template("index.html")

@app.route("/reload")
def reload():
    with open("app.py","a") as f:
        f.write(str(random.random())[0])

app.run(host = '0.0.0.0',debug=True)

# reload code

c = 000000000000000000000000000000000
00000000
0000
