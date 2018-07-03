package scaleform.clik.managers
{
    import flash.display.Stage;
    import flash.display.MovieClip;
    import flash.events.Event;
    import flash.display.Sprite;
    import flash.display.DisplayObject;
    import flash.display.DisplayObjectContainer;
    import net.wg.utils.IEventCollector;
    import flash.geom.Point;
    import scaleform.clik.controls.ScrollingList;
    import net.wg.infrastructure.interfaces.IDynamicContent;
    import scaleform.gfx.FocusManager;
    
    public class PopUpManager
    {
        
        protected static var initialized:Boolean = false;
        
        protected static var _stage:Stage;
        
        protected static var _defaultPopupCanvas:MovieClip;
        
        protected static var _modalMc:Sprite;
        
        protected static var _modalBg:Sprite;
         
        public function PopUpManager()
        {
            super();
        }
        
        public static function init(stage:Stage) : void
        {
            if(initialized)
            {
                return;
            }
            PopUpManager._stage = stage;
            _defaultPopupCanvas = new MovieClip();
            _defaultPopupCanvas.addEventListener(Event.REMOVED,handleRemovePopup,false,0,true);
            _stage.addChild(_defaultPopupCanvas);
            initialized = true;
        }
        
        public static function get popupCanvas() : MovieClip
        {
            return _defaultPopupCanvas;
        }
        
        public static function show(mc:DisplayObject, x:Number = 0, y:Number = 0, scope:DisplayObjectContainer = null) : void
        {
            if(!_stage)
            {
                return;
            }
            var events:IEventCollector = App.utils.events;
            events.disableDisposingForObj(mc);
            if(mc.parent)
            {
                mc.parent.removeChild(mc);
            }
            handleStageAddedEvent(null);
            _defaultPopupCanvas.addChild(mc);
            events.enableDisposingForObj(mc);
            if(!scope)
            {
                scope = _stage;
            }
            var p:Point = new Point(x,y);
            p = scope.localToGlobal(p);
            if(mc is ScrollingList || mc is IDynamicContent)
            {
                p.x = p.x / App.appScale >> 0;
                p.y = p.y / App.appScale >> 0;
            }
            mc.x = p.x;
            mc.y = p.y;
            _stage.setChildIndex(_defaultPopupCanvas,_stage.numChildren - 1);
            _stage.addEventListener(Event.ADDED,PopUpManager.handleStageAddedEvent,false,0,true);
        }
        
        public static function showModal(mc:Sprite, mcX:Number = 0, mcY:Number = 0, bg:Sprite = null, controllerIdx:uint = 0, newFocus:Sprite = null) : void
        {
            if(!_stage)
            {
                return;
            }
            if(_modalMc)
            {
                _defaultPopupCanvas.removeChild(_modalMc);
            }
            if(mc == null)
            {
                return;
            }
            if(bg == null)
            {
                bg = new Sprite();
                bg.graphics.lineStyle(0,16777215,0);
                bg.graphics.beginFill(16777215,0);
                bg.graphics.drawRect(0,0,_stage.stageWidth,_stage.stageHeight);
                bg.graphics.endFill();
            }
            _modalMc = mc;
            _modalBg = bg;
            _modalMc.x = mcX;
            _modalMc.y = mcY;
            _defaultPopupCanvas.addChild(_modalBg);
            _defaultPopupCanvas.addChild(_modalMc);
            FocusHandler.getInstance().setFocus(newFocus,controllerIdx,false);
            FocusManager.setModalClip(_modalMc,controllerIdx);
            _modalMc.addEventListener(Event.REMOVED_FROM_STAGE,handleRemoveModalMc,false,0,true);
            _stage.addEventListener(Event.ADDED,PopUpManager.handleStageAddedEvent,false,0,true);
        }
        
        protected static function handleStageAddedEvent(e:Event) : void
        {
            _stage.setChildIndex(_defaultPopupCanvas,_stage.numChildren - 1);
        }
        
        protected static function handleRemovePopup(e:Event) : void
        {
            removeAddedToStageListener();
        }
        
        protected static function handleRemoveModalMc(e:Event) : void
        {
            _modalBg.removeEventListener(Event.REMOVED_FROM_STAGE,handleRemoveModalMc,false);
            if(_modalBg)
            {
                _defaultPopupCanvas.removeChild(_modalBg);
            }
            _modalMc = null;
            _modalBg = null;
            FocusManager.setModalClip(null);
            removeAddedToStageListener();
        }
        
        protected static function removeAddedToStageListener() : void
        {
            if(_defaultPopupCanvas.numChildren == 0 && _modalMc == null)
            {
                _stage.removeEventListener(Event.ADDED,PopUpManager.handleStageAddedEvent,false);
            }
        }
    }
}
