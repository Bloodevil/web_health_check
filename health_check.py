import httplib
import urllib
import urllib2
import time


def use_httplib():
    """Use httplib module
    refer : https://docs.python.org/2/library/httplib.html
    """
    print '#' * 30
    print '# Use httplib #'

    start = time.time()
    print 'start:', start

    conn = httplib.HTTPConnection('www.stackoverflow.com')
    conn.request('GET', '/')    # GET, HEAD, POST, ....

    # Should be called after a request is sent to get the response from the server.
    # Returns an HTTPResponse instance.
    res = conn.getresponse()

    # netstat -napc | grep :80
    conn.close()    # Close the connection to the server

    data = res.read()
    print 'data:', data

    end = time.time()
    print 'end:', end

    elapsed_time = end - start
    print 'elapsed_time:', elapsed_time

    print res.status, ':', res.reason
    print '#' * 30 + '\n\n'


def use_urllib():
    print '#' * 30
    print '# Use urllib #'

    start = time.time()
    print 'start:', start

    res = urllib.urlopen("http://www.stackoverflow.com")
    end = time.time()
    print 'end:', end

    print dir(res)
    print 'info:', res.info()
    print 'headers:', res.headers
    print 'geturl:', res.geturl()
    print 'code:', res.getcode()
    # print 'data:', res.read()  #

    res.close()

    diff = end - start
    print 'diff:', diff
    print '#' * 30 + '\n\n'


def main():
    use_httplib()
    use_urllib()





if __name__ == '__main__':
    main()
