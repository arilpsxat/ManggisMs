# @author Aril Psxat

from requests import post
from json import loads
from datetime import datetime
from pytz import timezone
from re import match

class Telegram:
    def __init__(self, bot_token, time_zone):
        self.url = 'https://api.telegram.org/bot' + bot_token + '/'
        self.timezone = time_zone
        self.response = post(self.url + 'getUpdates', {'offset': -1})
        if self.response.ok == True:
            if loads(self.response.text)['result'] == []:
                print('Silahkan kirim pesan terlebih dahulu ke bot anda!.')
                exit()
            else:
                print('Bot running ...')
                self.offset = loads(self.response.text)['result'][0]['update_id'] + 1
        else:
            if self.response.status_code == 401:
                print('Ada kesalahan pada token bot, silahkan cek kembali token bot anda!.')
                exit()
            else:
                print(str(self.response.status_code) + ' ERROR\nDescription: ' + loads(self.response.text)['description'])
                exit()
        
    @property
    def centMessage(self):
        self.response = post(self.url + 'getUpdates', {'offset': self.offset})
        if self.response.ok == True:
            if loads(self.response.text)['result'] == []:
                return False
            else:
                self.update = loads(self.response.text)['result'][0]
                try:
                    self.aa = self.update['message']
                except:
                    self.aa = None
                finally:
                    try:
                        self.ab = self.aa['from']
                    except:
                        self.ab = None
                    finally:
                        try:
                            self.ac = self.ab['id']
                        except:
                            self.ac = 404
                        finally:
                            try:
                                self.ad = self.ab['first_name']
                            except:
                                self.ad = 'None'
                            finally:
                                try:
                                    self.ae = self.ab['last_name']
                                except:
                                    self.ae = 'None'
                                finally:
                                    try:
                                        self.af = self.ab['username']
                                    except:
                                        self.af = 'None'
                                    finally:
                                        try:
                                            self.ag = self.aa['date']
                                        except:
                                            self.ag = 404
                                        finally:
                                            try:
                                                self.ah = self.aa['chat']
                                            except:
                                                self.ah = None
                                            finally:
                                                try:
                                                    self.ai = self.ah['id']
                                                except:
                                                    self.ai = 404
                                                finally:
                                                    try:
                                                        self.aj = self.ah['type']
                                                    except:
                                                        self.aj = 'None'
                                                    finally:
                                                        try:
                                                            self.ak = self.ah['title']
                                                        except:
                                                            self.ak = 'None'
                                                        finally:
                                                            try:
                                                                self.al = self.ah['username']
                                                            except:
                                                                self.al = 'None'
                                                            finally:
                                                                try:
                                                                    self.am = self.ah['first_name']
                                                                except:
                                                                    self.am = 'None'
                                                                finally:
                                                                    try:
                                                                        self.an = self.ah['last_name']
                                                                    except:
                                                                        self.an = 'None'
                                                                    finally:
                                                                        try:
                                                                            self.ao = self.aa['text']
                                                                        except:
                                                                            self.ao = 'None'
                                                                        finally:
                                                                            try:
                                                                                self.ap = self.aa['caption']
                                                                            except:
                                                                                self.ap = 'None'
                self.offset = self.offset + 1
                return True
        else:
            print(str(self.response.status_code) + ' ERROR\nDescription: ' + loads(self.response.text)['description'])
            exit()
        
    def cektMessage(self, **kwargs):
        self.cme = []
        self.dtt = datetime.now(timezone(self.timezone))
        self.dtthour = int(self.dtt.strftime('%-H'))
        self.dttmin = int(self.dtt.strftime('%-M'))
        self.dttday = int(self.dtt.strftime('%w'))
        self.dttdom = int(self.dtt.strftime('%-d'))
        self.dttmonth = int(self.dtt.strftime('%-m'))
        for a in kwargs:
            if a == 'mtext':
                self.mtext = False
                for b in kwargs['mtext']:
                    if match(b, self.ao):
                        self.mtext = True
                        self.cme.append(True)
                if self.mtext != True:
                    self.cme.append(False)
            elif a == 'mfid':
                if self.ac in kwargs['mfid']:
                    self.cme.append(True)
                else:
                    self.cme.append(False)
            elif a == 'mctype':
                if self.aj in kwargs['mctype']:
                    self.cme.append(True)
                else:
                    self.cme.append(False)
            elif a == 'mform':
                self.mform = False
                for c in kwargs['mform']:
                    if c in self.aa:
                        self.mform = True
                        self.cme.append(True)
                if self.mform != True:
                    self.cme.append(False)
            elif a == 'mcapt':
                self.mcapt = False
                for d in kwargs['mcapt']:
                    if match(d, self.ap):
                        self.mcapt = True
                        self.cme.append(True)
                if self.mcapt != True:
                    self.cme.append(False)
            elif a == 'mctitle':
                self.mctitle = False
                for e in kwargs['mctitle']:
                    if match(e, self.ak):
                        self.mctitle = True
                        self.cme.append(True)
                if self.mctitle != True:
                    self.cme.append(False)
            elif a == 'mfusername':
                if kwargs['mfusername'][0] == True:
                    if 'username' in self.ah:
                        self.cme.append(True)
                    else:
                        self.cme.append(False)
                else:
                    if 'username' not in self.ah:
                        self.cme.append(True)
                    else:
                        self.cme.append(False)
            elif a == 'clock':
                if kwargs['clock'][0] == self.dtthour:
                    if kwargs['clock'][1] == self.dttmin:
                        if kwargs['clock'][2] == self.dtthour:
                            if kwargs['clock'][3] == self.dttmin:
                                self.cme.append(True)
                            elif kwargs['clock'][3] > self.dttmin:
                                self.cme.append(True)
                            else:
                                self.cme.append(False)
                        elif kwargs['clock'][2] > self.dtthour:
                            self.cme.append(True)
                        else:
                            self.cme.append(False)
                    elif kwargs['clock'][1] < self.dttmin:
                        if kwargs['clock'][2] == self.dtthour:
                            if kwargs['clock'][3] == self.dttmin:
                                self.cme.append(True)
                            elif kwargs['clock'][3] > self.dttmin:
                                self.cme.append(True)
                            else:
                                self.cme.append(False)
                        elif kwargs['clock'][2] > self.dtthour:
                            self.cme.append(True)
                        else:
                            self.cme.append(False)
                    else:
                        self.cme.append(False)
                elif kwargs['clock'][0] < self.dtthour:
                    if kwargs['clock'][2] == self.dtthour:
                        if kwargs['clock'][3] == self.dttmin:
                            self.cme.append(True)
                        elif kwargs['clock'][3] > self.dttmin:
                            self.cme.append(True)
                        else:
                            self.cme.append(False)
                    elif kwargs['clock'][2] > self.dtthour:
                        self.cme.append(True)
                    else:
                        self.cme.append(False)
                else:
                    self.cme.append(False)
            elif a == 'day':
                if self.dttday in kwargs['day']:
                    self.cme.append(True)
                else:
                    self.cme.append(False)
            elif a == 'dom':
                if self.dttdom in kwargs['dom']:
                    self.cme.append(True)
                else:
                    self.cme.append(False)
            elif a == 'month':
                if self.dttmonth in kwargs['month']:
                    self.cme.append(True)
                else:
                    self.cme.append(False)
        if False not in self.cme:
            return True
        else:
            return False
        
    def postReq(self, method, **parameter):
        self.response = post(self.url + method, parameter)
        self.reqres = loads(self.response.text)
        
