package scaleform.clik.managers
{
    import flash.events.EventDispatcher;
    import flash.display.Stage;
    import flash.events.KeyboardEvent;
    import scaleform.clik.constants.NavigationCode;
    import flash.ui.Keyboard;
    import scaleform.gfx.KeyboardEventEx;
    import scaleform.clik.constants.InputValue;
    import scaleform.clik.ui.InputDetails;
    import scaleform.clik.events.InputEvent;
    
    public class InputDelegate extends EventDispatcher
    {
        
        private static var instance:scaleform.clik.managers.InputDelegate;
        
        public static const MAX_KEY_CODES:uint = 1000;
        
        public static const KEY_PRESSED:uint = 1;
        
        public static const KEY_SUPRESSED:uint = 2;
         
        public var stage:Stage;
        
        public var externalInputHandler:Function;
        
        protected var keyHash:Array;
        
        public function InputDelegate()
        {
            super();
            this.keyHash = [];
        }
        
        public static function getInstance() : scaleform.clik.managers.InputDelegate
        {
            if(instance == null)
            {
                instance = new scaleform.clik.managers.InputDelegate();
            }
            return instance;
        }
        
        public function initialize(stage:Stage) : void
        {
            this.stage = stage;
            stage.addEventListener(KeyboardEvent.KEY_DOWN,this.handleKeyDown,false,0,true);
            stage.addEventListener(KeyboardEvent.KEY_UP,this.handleKeyUp,false,0,true);
        }
        
        public function setKeyRepeat(code:Number, repeat:Boolean, controllerIndex:uint = 0) : void
        {
            var index:uint = controllerIndex * MAX_KEY_CODES + code;
            if(repeat)
            {
                this.keyHash[index] = this.keyHash[index] & ~KEY_SUPRESSED;
            }
            else
            {
                this.keyHash[index] = this.keyHash[index] | KEY_SUPRESSED;
            }
        }
        
        public function inputToNav(type:String, code:Number, shiftKey:Boolean = false, value:* = null) : String
        {
            if(this.externalInputHandler != null)
            {
                return this.externalInputHandler(type,code,value);
            }
            if(type == "key")
            {
                switch(code)
                {
                    case Keyboard.UP:
                        return NavigationCode.UP;
                    case Keyboard.DOWN:
                        return NavigationCode.DOWN;
                    case Keyboard.LEFT:
                        return NavigationCode.LEFT;
                    case Keyboard.RIGHT:
                        return NavigationCode.RIGHT;
                    case Keyboard.ENTER:
                    case Keyboard.SPACE:
                        return NavigationCode.ENTER;
                    case Keyboard.BACKSPACE:
                        return NavigationCode.BACK;
                    case Keyboard.TAB:
                        if(shiftKey)
                        {
                            return NavigationCode.SHIFT_TAB;
                        }
                        return NavigationCode.TAB;
                    case Keyboard.HOME:
                        return NavigationCode.HOME;
                    case Keyboard.END:
                        return NavigationCode.END;
                    case Keyboard.PAGE_DOWN:
                        return NavigationCode.PAGE_DOWN;
                    case Keyboard.PAGE_UP:
                        return NavigationCode.PAGE_UP;
                    case Keyboard.ESCAPE:
                        return NavigationCode.ESCAPE;
                }
            }
            return null;
        }
        
        public function readInput(type:String, code:int, callBack:Function) : Object
        {
            return null;
        }
        
        protected function handleKeyDown(event:KeyboardEvent) : void
        {
            var sfEvent:KeyboardEventEx = event as KeyboardEventEx;
            var controllerIdx:uint = sfEvent == null?uint(0):uint(sfEvent.controllerIdx);
            var code:Number = event.keyCode;
            var keyStateIndex:uint = controllerIdx * MAX_KEY_CODES + code;
            var keyState:uint = this.keyHash[keyStateIndex];
            if(keyState & KEY_PRESSED)
            {
                if((keyState & KEY_SUPRESSED) == 0)
                {
                    this.handleKeyPress(InputValue.KEY_HOLD,code,controllerIdx,event.ctrlKey,event.altKey,event.shiftKey);
                }
            }
            else
            {
                this.handleKeyPress(InputValue.KEY_DOWN,code,controllerIdx,event.ctrlKey,event.altKey,event.shiftKey);
                this.keyHash[keyStateIndex] = this.keyHash[keyStateIndex] | KEY_PRESSED;
            }
        }
        
        protected function handleKeyUp(event:KeyboardEvent) : void
        {
            var sfEvent:KeyboardEventEx = event as KeyboardEventEx;
            var controllerIdx:uint = sfEvent == null?uint(0):uint(sfEvent.controllerIdx);
            var code:Number = event.keyCode;
            var keyStateIndex:uint = controllerIdx * MAX_KEY_CODES + code;
            this.keyHash[keyStateIndex] = this.keyHash[keyStateIndex] & ~KEY_PRESSED;
            this.handleKeyPress(InputValue.KEY_UP,code,controllerIdx,event.ctrlKey,event.altKey,event.shiftKey);
        }
        
        protected function handleKeyPress(type:String, code:Number, controllerIdx:Number, ctrl:Boolean, alt:Boolean, shift:Boolean) : void
        {
            var details:InputDetails = new InputDetails("key",code,type,this.inputToNav("key",code,shift),controllerIdx,ctrl,alt,shift);
            dispatchEvent(new InputEvent(InputEvent.INPUT,details));
        }
    }
}
