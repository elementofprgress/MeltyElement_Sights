class com.greensock.dataTransfer.XMLParser
{
    var parse, loaded, _results, _xmlUrl, _onComplete, keepRootNode, parseLineBreaks, _xml, __get__bytesLoaded, __get__bytesTotal, __get__percentLoaded, __get__xml;
    static var _all, __get__active;
    function XMLParser()
    {
        parse = initLoad;
        loaded = false;
        if (com.greensock.dataTransfer.XMLParser._all == undefined)
        {
            _all = [];
        } // end if
        com.greensock.dataTransfer.XMLParser._all.push(this);
    } // End of the function
    static function load($url, $onComplete, $results, $keepRootNode, $parseLineBreaks)
    {
        var _loc1 = new com.greensock.dataTransfer.XMLParser();
        _loc1.initLoad($url, $onComplete, $results, $keepRootNode, $parseLineBreaks);
        return (_loc1);
    } // End of the function
    static function sendAndLoad($toSend, $url, $onComplete, $results, $keepRootNode, $parseLineBreaks)
    {
        var _loc1 = new com.greensock.dataTransfer.XMLParser();
        _loc1.initSendAndLoad($toSend, $url, $onComplete, $results, $keepRootNode, $parseLineBreaks);
        return (_loc1);
    } // End of the function
    function initLoad($url, $onComplete, $results, $keepRootNode, $parseLineBreaks)
    {
        _results = $results || {};
        _xmlUrl = $url;
        _onComplete = $onComplete;
        keepRootNode = $keepRootNode;
        parseLineBreaks = $parseLineBreaks;
        _xml = new XML();
        _xml.ignoreWhite = true;
        _xml.onData = mx.utils.Delegate.create(this, onData);
        loaded = false;
        _xml.load(_xmlUrl);
    } // End of the function
    function initSendAndLoad($toSend, $url, $onComplete, $results, $keepRootNode, $parseLineBreaks)
    {
        _results = $results || {};
        _xmlUrl = $url;
        _onComplete = $onComplete;
        keepRootNode = $keepRootNode;
        parseLineBreaks = $parseLineBreaks;
        var _loc2;
        if ($toSend instanceof XML)
        {
            _loc2 = (XML)($toSend);
        }
        else
        {
            _loc2 = com.greensock.dataTransfer.XMLParser.objectToXML($toSend);
        } // end else if
        _xml = new XML();
        _xml.ignoreWhite = true;
        _xml.onData = mx.utils.Delegate.create(this, onData);
        loaded = false;
        _loc2.sendAndLoad(_xmlUrl, _xml);
    } // End of the function
    function onData($xml)
    {
        if ($xml == undefined)
        {
            this.parseLoadedXML(false);
        }
        else
        {
            _xml.parseXML($xml);
            loaded = true;
            this.parseLoadedXML(true);
        } // end else if
    } // End of the function
    function parseLoadedXML($success)
    {
        if ($success == false)
        {
            trace ("XML FAILED TO LOAD! (" + _xmlUrl + ")");
            this._onComplete(false);
            return;
        } // end if
        com.greensock.dataTransfer.XMLParser.XMLToObject(_xml, _results, keepRootNode, parseLineBreaks);
        this._onComplete(true, _results, _xml);
    } // End of the function
    static function XMLToObject($xml, $results, $keepRootNode, $parseLineBreaks)
    {
        var _loc8 = $xml;
        $results = $results || {};
        var _loc1 = _loc8.firstChild;
        var _loc7 = _loc8.firstChild;
        _loc8.obj = $results;
        if ($keepRootNode != true)
        {
            _loc1 = _loc1.firstChild;
            _loc7 = _loc8.firstChild.lastChild;
            _loc8.firstChild.obj = $results;
        } // end if
        while (_loc1 != undefined)
        {
            if (_loc1.nodeName == null && _loc1.nodeType == 3)
            {
                _loc1.parentNode.obj.nodeValue = com.greensock.dataTransfer.XMLParser.clean(_loc1.nodeValue, $parseLineBreaks);
            }
            else
            {
                _loc1.nodeName = _loc1.nodeName.split("-").join("_");
                var _loc3 = {};
                for (var _loc6 in _loc1.attributes)
                {
                    _loc3[_loc6] = com.greensock.dataTransfer.XMLParser.clean(_loc1.attributes[_loc6], $parseLineBreaks);
                } // end of for...in
                var _loc4 = _loc1.parentNode.obj;
                if (_loc4[_loc1.nodeName] == undefined)
                {
                    _loc4[_loc1.nodeName] = [];
                } // end if
                _loc1.obj = _loc3;
                _loc4[_loc1.nodeName].push(_loc3);
            } // end else if
            if (_loc1.childNodes.length > 0)
            {
                _loc1 = _loc1.childNodes[0];
                continue;
            } // end if
            for (var _loc2 = _loc1; _loc2.nextSibling == undefined && _loc2.parentNode != undefined; _loc2 = _loc2.parentNode)
            {
            } // end of for
            _loc1 = _loc2.nextSibling;
            if (_loc2 == _loc7)
            {
                _loc1 = undefined;
            } // end if
        } // end while
        return ($results);
    } // End of the function
    static function clean($s, $parseLineBreaks)
    {
        if (!isNaN(Number($s)) && $s != "" && $s.charAt(0) != "0" && com.greensock.dataTransfer.XMLParser.containsNoLetters($s))
        {
            return (Number($s));
        }
        else if ($s == "true")
        {
            return (true);
        }
        else if ($s == "false")
        {
            return (false);
        }
        else if ($parseLineBreaks)
        {
            return ($s.split("\\n").join("\n"));
        }
        else
        {
            return ($s);
        } // end else if
    } // End of the function
    static function containsNoLetters($s)
    {
        var _loc3 = $s.length;
        var _loc2;
        for (var _loc1 = 0; _loc1 < _loc3; ++_loc1)
        {
            _loc2 = $s.charCodeAt(_loc1);
            if (_loc2 < 48 || _loc2 > 57)
            {
                return (false);
            } // end if
        } // end of for
        return (true);
    } // End of the function
    static function objectToXML($o, $rootNodeName)
    {
        if ($rootNodeName == undefined)
        {
            $rootNodeName = "XML";
        } // end if
        var _loc6 = new XML();
        var _loc4 = _loc6.createElement($rootNodeName);
        var _loc5 = [];
        var _loc1;
        var _loc2;
        var _loc7;
        for (var _loc2 in $o)
        {
            _loc5.push(_loc2);
        } // end of for...in
        for (var _loc2 = _loc5.length - 1; _loc2 >= 0; --_loc2)
        {
            _loc1 = _loc5[_loc2];
            if (typeof($o[_loc1]) == "object" && $o[_loc1].length > 0)
            {
                com.greensock.dataTransfer.XMLParser.arrayToNodes($o[_loc1], _loc4, _loc6, _loc1);
                continue;
            } // end if
            if (_loc1 == "nodeValue")
            {
                _loc7 = _loc6.createTextNode($o.nodeValue);
                _loc4.appendChild(_loc7);
                continue;
            } // end if
            _loc4.attributes[_loc1] = $o[_loc1];
        } // end of for
        _loc6.appendChild(_loc4);
        return (_loc6);
    } // End of the function
    static function arrayToNodes($ar, $parentNode, $xml, $nodeName)
    {
        var _loc9 = [];
        var _loc6;
        var _loc1;
        var _loc4;
        var _loc2;
        var _loc5;
        var _loc3;
        for (var _loc5 = $ar.length - 1; _loc5 >= 0; --_loc5)
        {
            _loc4 = $xml.createElement($nodeName);
            _loc2 = $ar[_loc5];
            _loc6 = [];
            for (var _loc3 in _loc2)
            {
                _loc6.push(_loc3);
            } // end of for...in
            for (var _loc3 = _loc6.length - 1; _loc3 >= 0; --_loc3)
            {
                _loc1 = _loc6[_loc3];
                if (typeof(_loc2[_loc1]) == "object" && _loc2[_loc1].length > 0)
                {
                    com.greensock.dataTransfer.XMLParser.arrayToNodes(_loc2[_loc1], _loc4, $xml, _loc1);
                    continue;
                } // end if
                if (_loc1 != "nodeValue")
                {
                    _loc4.attributes[_loc1] = _loc2[_loc1];
                    continue;
                } // end if
                var _loc7 = $xml.createTextNode(_loc2.nodeValue);
                _loc4.appendChild(_loc7);
            } // end of for
            _loc9.push(_loc4);
        } // end of for
        for (var _loc5 = _loc9.length - 1; _loc5 >= 0; --_loc5)
        {
            $parentNode.appendChild(_loc9[_loc5]);
        } // end of for
    } // End of the function
    function cancel()
    {
        _xml.onData = null;
    } // End of the function
    function destroy()
    {
        this.cancel();
        delete this._xml;
        for (var _loc2 = com.greensock.dataTransfer.XMLParser._all.length - 1; _loc2 >= 0; --_loc2)
        {
            if (this == com.greensock.dataTransfer.XMLParser._all[_loc2])
            {
                com.greensock.dataTransfer.XMLParser._all.splice(_loc2, 1);
            } // end if
        } // end of for
    } // End of the function
    static function get active()
    {
        if (com.greensock.dataTransfer.XMLParser._all.length > 0)
        {
            return (true);
        }
        else
        {
            return (false);
        } // end else if
    } // End of the function
    function get percentLoaded()
    {
        //return (this.bytesLoaded() / this.__get__bytesTotal() * 100);
    } // End of the function
    function get xml()
    {
        return (_xml);
    } // End of the function
    function get bytesLoaded()
    {
        return (_xml.getBytesLoaded() || 0);
    } // End of the function
    function get bytesTotal()
    {
        if (loaded)
        {
            return (_xml.getBytesTotal() || 0);
        }
        else
        {
            return (_xml.getBytesTotal() || 1024);
        } // end else if
    } // End of the function
} // End of Class
