## network interface
  - in charge of hardware
    - network adapter
  - mac address
    - 40-49-0F-80-C3-2F
    - manufacturer ID
    - product ID
---
## ARP
  - request packet
    - target mac
      00:00:00:00:00:00
      target IP
      192.168.1.4
  - response packet
    - sender mac
     28:5A:EB:67:44:86
     sender IP
     192.168.1.4
---
## MAC ? IP?
  - MAC for NEXT hardware in PATH
  - IP for LAST computer 
---
## internet
  - sends data to destination computer
    - identify computer by IP address 
  - IP address
    - public IP
      - globally unique IP
    - private IP
      - for private network
  - DNS
    - google.com <-> 216.58.203.14
---
## NAT
  - network address translation
  - private IP -> public IP
  - but port is same
  - problem
    - if same port from different hosts
  - NAPT(network address port translation)
    - private IP -> public IP
    - change port if same port
---

## transport
  - sends data to destination process(application)
    - identify application by port
  - port
    - well-known port : 0~1023
      - SERVER program
    - registered port : 1024 ~ 49151
    - dynamic port : 49152~65535
      - CLIENT program
---
## well-kown port
  - 20, 21 : FTP
  - 22 : SSH
  - 23 : Telnet
  - 25 : SMTP(mail send)
  - 80 : HTTP(web)
  - 110 : POP3(main receive)
  - 443 : HTTPS 
---
## TCP & UDP
  - TCP
    - precision
  - UDP
    - speed
---
## application
  - provides service to user
  - protocol
    - http, ftp, telnet, ssh, smtp, pop
---
## web client - 1
  - URL request by web browser
    - URL of web page
---
## URL
  - URL(Uniform resource locator)
    - not web site address!!
    - all resources on the net
    - complies with protocol
  - http request
  - http://www.company.co.kr/picture/food.jpg
  - schema://host.domain/directory/file
---
## web server 
  - HTML response by server
---
## web client - 2
  - read HTML in web browser
  - if needed, requests CSS, JPEG, JS
```html
<!DOCTYPE html>
<html>
    <head>...</head>
    <body>
        ...
        <img src = "delicious_food.jpg">
        <script>...</script>
    </body>
</html>
```
---
## AJAX
  - Asynchronous javascript and XML
  - request from not browser but javascript
  - NOT draw all of renewed page
  - draw changed part of page 
---
## cookie
  - browser checks 'Set-Cookie:' in response
  - saves cookie in local disc
    - SESSIONID
    - expires
    - domain, path
---
## login
  - user sends ID, password
  - web server issues SESSIONID
  - sends cookie
  - user sends requests with SESSIONID  



