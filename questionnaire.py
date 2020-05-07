from flask import Flask, render_template, request
app = Flask(__name__)

name_list=['伊澤啓太','石田鉱大','上田愛佳','長島芽依','服部真由',
           '上西杏奈','笠原奈津美','加納穂乃香','川崎理瑚','川瀬悠里','中原茉保','丹羽良徳','三宅陽平','宮部亜里紗'
           '天部一貴','市川天音','大野稚菜','下川航','杉浦夢歩','生井貴大','前島由依','水谷沙希','村瀬泰介','山本佳奈'
           '今村茉由','城諒武','都築美奈','中嶋千賀','山中真名',
           '小川芹葉','加藤総一郎','田口珠理','武内杏樹','橘楓','中村ちゆり','永山治佳','安永晴香']

@app.route("/github.com/tsuteto-ryb/questionnaire/edit/master/")
def index():
    return render_template('questionnaire-toppage.html')

@app.route("/github.com/tsuteto-ryb/questionnaire/edit/master/confirmation")
def confirmation():
    if request.form.get('name','') in name_list:
        name=request.form.get('name')
        return redirect(url_for('entry'),name=name)

@app.route("/github.com/tsuteto-ryb/questionnaire/edit/master/entry")
def entry():
    return render_template('questionnaire.html',name=name,name_list=name_list)
