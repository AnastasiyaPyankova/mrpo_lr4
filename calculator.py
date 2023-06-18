from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True
history = list()


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def calculator():
    num1 = request.form.get("num1", type=int)
    num2 = request.form.get("num2", type=int)
    sign = request.form.get("sign", type=str)
    if sign == '+':
        num3 = num1 + num2
    elif sign == '-':
        num3 = num1 - num2
    elif sign == '*':
        num3 = num1 * num2
    elif sign == '/':
        if num2 == 0:
            num3 = 'Делитель=0'
        else:
            num3 = num1 / num2
    else:
        num3 = 0
    res = num3
    history.append([num1, sign, num2, '=', res])
    return render_template('index.html', result=res, history=history)


if __name__ == '__main__':
    app.run()

