﻿class gfx.core.UIComponent extends MovieClip
{
    var _width, _height, useHandCursor, __get__disabled, _visible, dispatchEvent, __get__visible, __get__width, __get__height, __get__focused, __get__displayFocus, invalidationIntervalID, _name, _yscale, _xscale, hitTest, __set__disabled, __set__displayFocus, __set__focused, __set__height, __set__visible, __set__width;
    function UIComponent()
    {
        super();
        gfx.events.EventDispatcher.initialize(this);
    } // End of the function
    function onLoad()
    {
        if (__width == Number.NaN)
        {
            __width = _width;
        } // end if
        if (__height == Number.NaN)
        {
            __height = _height;
        } // end if
        initialized = true;
        this.configUI();
        this.validateNow();
        if (_focused && Selection.getFocus() == null)
        {
            gfx.managers.FocusHandler.__get__instance().onSetFocus(null, this);
        } // end if
    } // End of the function
    static function createInstance(context, symbol, name, depth, initObj)
    {
        var _loc1 = context.attachMovie(symbol, name, depth, initObj);
        if (_loc1.invalidate)
        {
            _loc1.invalidate();
        } // end if
        return (_loc1);
    } // End of the function
    function get disabled()
    {
        return (_disabled);
    } // End of the function
    function set disabled(value)
    {
        _disabled = value;
        super.enabled = !value;
        useHandCursor = !value;
        this.invalidate();
        null;
        null;
        null;
        null;
        //return (this.disabled());
        null;
    } // End of the function
    function get visible()
    {
        return (_visible);
    } // End of the function
    function set visible(value)
    {
        if (_visible == value)
        {
            return;
        } // end if
        _visible = value;
        if (!initialized)
        {
            return;
        } // end if
        var _loc3 = value ? ("show") : ("hide");
        this.dispatchEvent({type: _loc3});
        null;
        null;
        null;
        null;
        //return (this.visible());
        null;
    } // End of the function
    function get width()
    {
        return (__width);
    } // End of the function
    function set width(value)
    {
        this.setSize(value, __height || _height);
        null;
        null;
        null;
        null;
        //return (this.width());
        null;
    } // End of the function
    function get height()
    {
        return (__height);
    } // End of the function
    function set height(value)
    {
        this.setSize(__width || _width, value);
        null;
        null;
        null;
        null;
        //return (this.height());
        null;
    } // End of the function
    function setSize(width, height)
    {
        if (__width == width && __height == height)
        {
            return;
        } // end if
        __width = width;
        __height = height;
        sizeIsInvalid = true;
        this.invalidate();
    } // End of the function
    function get focused()
    {
        return (_focused);
    } // End of the function
    function set focused(value)
    {
        if (value == _focused)
        {
            return;
        } // end if
        _focused = value;
        if (!value && Selection.getFocus() == this)
        {
            Selection.setFocus(null);
        }
        else if (value && Selection.getFocus() != this)
        {
            Selection.setFocus(this);
        } // end else if
        this.changeFocus();
        var _loc3 = value ? ("focusIn") : ("focusOut");
        this.dispatchEvent({type: _loc3});
        null;
        null;
        null;
        null;
        //return (this.focused());
        null;
    } // End of the function
    function get displayFocus()
    {
        return (_displayFocus);
    } // End of the function
    function set displayFocus(value)
    {
        if (value == _displayFocus)
        {
            return;
        } // end if
        _displayFocus = value;
        this.changeFocus();
        null;
        null;
        null;
        null;
        //return (this.displayFocus());
        null;
    } // End of the function
    function handleInput(details, pathToFocus)
    {
        if (pathToFocus != null && pathToFocus.length > 0)
        {
            var _loc2 = pathToFocus[0].handleInput(details, pathToFocus.slice(1));
            if (_loc2)
            {
                return (_loc2);
            } // end if
        } // end if
        return (false);
    } // End of the function
    function invalidate()
    {
        if (invalidationIntervalID)
        {
            return;
        } // end if
        invalidationIntervalID = setInterval(this, "validateNow", 1);
    } // End of the function
    function validateNow()
    {
        clearInterval(invalidationIntervalID);
        delete this.invalidationIntervalID;
        if (!initialized)
        {
            this.onLoad();
            return;
        } // end if
        this.draw();
        sizeIsInvalid = false;
    } // End of the function
    function toString()
    {
        return ("[Scaleform UIComponent " + _name + "]");
    } // End of the function
    function configUI()
    {
    } // End of the function
    function initSize()
    {
        var _loc3 = __width == 0 ? (_width) : (__width);
        var _loc2 = __height == 0 ? (_height) : (__height);
        _xscale = _yscale = 100;
        this.setSize(_loc3, _loc2);
    } // End of the function
    function draw()
    {
    } // End of the function
    function changeFocus()
    {
    } // End of the function
    function onMouseWheel(delta, target)
    {
        if (this.__get__visible() && this.hitTest(_root._xmouse, _root._ymouse, true))
        {
            this.scrollWheel(delta > 0 ? (1) : (-1));
        } // end if
    } // End of the function
    function scrollWheel(delta)
    {
    } // End of the function
    var initialized = false;
    var __width = Number.NaN;
    var __height = Number.NaN;
    var _disabled = false;
    var _focused = false;
    var _displayFocus = false;
    var sizeIsInvalid = false;
} // End of Class
