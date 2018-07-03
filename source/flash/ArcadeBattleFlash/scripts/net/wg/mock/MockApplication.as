package net.wg.mock
{
    import flash.events.EventDispatcher;
    import net.wg.app.IApplication;
    import net.wg.infrastructure.managers.IGlobalVarsManager;
    import net.wg.infrastructure.managers.ISoundManager;
    import net.wg.infrastructure.managers.ITooltipMgr;
    import net.wg.infrastructure.managers.IWaitingView;
    import net.wg.infrastructure.managers.IEnvironmentManager;
    import net.wg.infrastructure.interfaces.ICursor;
    import net.wg.infrastructure.managers.IContainerManager;
    import net.wg.utils.ITextManager;
    import net.wg.infrastructure.managers.IContextMenuManager;
    import net.wg.infrastructure.managers.IPopoverManager;
    import net.wg.infrastructure.managers.IColorSchemeManager;
    import net.wg.infrastructure.managers.IVoiceChatManager;
    import net.wg.utils.IGameInputManager;
    import net.wg.infrastructure.managers.ILoaderManager;
    import net.wg.infrastructure.managers.ICacheManager;
    import net.wg.utils.IUtils;
    import net.wg.utils.ITweenManager;
    import net.wg.infrastructure.interfaces.IManagedContainer;
    import net.wg.infrastructure.base.meta.ICacheManagerMeta;
    import net.wg.infrastructure.managers.IEventLogManager;
    import net.wg.infrastructure.base.meta.IGameInputManagerMeta;
    import net.wg.infrastructure.base.meta.IGlobalVarsMgrMeta;
    import net.wg.infrastructure.base.meta.ILoaderManagerMeta;
    import net.wg.infrastructure.managers.ITutorialManager;
    import net.wg.infrastructure.base.meta.IUtilsManagerMeta;
    import flash.display.Stage;
    import flash.display.DisplayObjectContainer;
    import net.wg.infrastructure.managers.IAtlasManager;
    
    public class MockApplication extends EventDispatcher implements IApplication
    {
         
        private var _globalVarsMgr:IGlobalVarsManager;
        
        private var _soundMgr:ISoundManager;
        
        private var _toolTipMgr:ITooltipMgr;
        
        private var _waiting:IWaitingView;
        
        private var _environment:IEnvironmentManager;
        
        private var _cursor:ICursor;
        
        private var _containerMgr:IContainerManager;
        
        private var _textMgr:ITextManager;
        
        private var _contextMenuMgr:IContextMenuManager;
        
        private var _popoverMgr:IPopoverManager;
        
        private var _colorSchemeMgr:IColorSchemeManager;
        
        private var _voiceChatMgr:IVoiceChatManager;
        
        private var _gameInputMgr:IGameInputManager;
        
        private var _loaderMgr:ILoaderManager;
        
        private var _cacheMgr:ICacheManager;
        
        private var _utils:IUtils;
        
        private var _tweenMgr:ITweenManager;
        
        public function MockApplication()
        {
            super();
            this._globalVarsMgr = new MockGlobalVarsManager();
            this._soundMgr = new MockSoundManager();
            this._toolTipMgr = new MockTooltipMgr();
            this._waiting = new MockWaitingView();
            this._environment = new MockEnvironmentManager();
            this._cursor = new MockCursor();
            this._containerMgr = new MockContainerManager();
            this._textMgr = new MockTextManager();
            this._contextMenuMgr = new MockContextMenuManager();
            this._popoverMgr = new MockPopoverManager();
            this._colorSchemeMgr = new MockColorSchemeManager();
            this._voiceChatMgr = new MockVoiceChatManager();
            this._gameInputMgr = new MockGameInputManager();
            this._loaderMgr = new MockLoaderManager();
            this._cacheMgr = new MockCacheManager();
            this._utils = new MockUtils();
            this._tweenMgr = new MockTweenManager();
        }
        
        public function as_dispose() : void
        {
        }
        
        public function as_isDAAPIInited() : Boolean
        {
            return false;
        }
        
        public function as_populate() : void
        {
        }
        
        public function as_registerManagers() : void
        {
        }
        
        public function as_setLibrariesList(list:Array) : void
        {
        }
        
        public function as_updateStage(w:Number, h:Number, scale:Number) : void
        {
        }
        
        public function getManagedContainer(type:String) : IManagedContainer
        {
            return null;
        }
        
        public function handleGlobalKeyEventS(command:String) : void
        {
        }
        
        public function onAsInitializationCompletedS() : void
        {
        }
        
        public function setCacheMgrS(mgr:ICacheManagerMeta) : void
        {
        }
        
        public function setColorSchemeMgrS(mgr:IColorSchemeManager) : void
        {
        }
        
        public function setContainerMgrS(mgr:IContainerManager) : void
        {
        }
        
        public function setContextMenuMgrS(mgr:IContextMenuManager) : void
        {
        }
        
        public function setEventLogMgrS(mgr:IEventLogManager) : void
        {
        }
        
        public function setGameInputMgrS(mgr:IGameInputManagerMeta) : void
        {
        }
        
        public function setGlobalVarsMgrS(mgr:IGlobalVarsMgrMeta) : void
        {
        }
        
        public function setLoaderMgrS(mgr:ILoaderManagerMeta) : void
        {
        }
        
        public function setPopoverMgrS(mgr:IPopoverManager) : void
        {
        }
        
        public function setSoundMgrS(mgr:ISoundManager) : void
        {
        }
        
        public function setTextMgrS(mgr:ITextManager) : void
        {
        }
        
        public function setTooltipMgrS(mgr:ITooltipMgr) : void
        {
        }
        
        public function setTutorialMgrS(mgr:ITutorialManager) : void
        {
        }
        
        public function setTweenMgrS(mgr:ITweenManager) : void
        {
        }
        
        public function setUtilsMgrS(mgr:IUtilsManagerMeta) : void
        {
        }
        
        public function setVoiceChatMgrS(mgr:IVoiceChatManager) : void
        {
        }
        
        public function get appWidth() : Number
        {
            return 0;
        }
        
        public function get appHeight() : Number
        {
            return 0;
        }
        
        public function get appScale() : Number
        {
            return 0;
        }
        
        public function get stage() : Stage
        {
            return null;
        }
        
        public function get systemMessages() : DisplayObjectContainer
        {
            return null;
        }
        
        public function get globalVarsMgr() : IGlobalVarsManager
        {
            return this._globalVarsMgr;
        }
        
        public function get soundMgr() : ISoundManager
        {
            return this._soundMgr;
        }
        
        public function get toolTipMgr() : ITooltipMgr
        {
            return this._toolTipMgr;
        }
        
        public function get waiting() : IWaitingView
        {
            return this._waiting;
        }
        
        public function get environment() : IEnvironmentManager
        {
            return this._environment;
        }
        
        public function get cursor() : ICursor
        {
            return this._cursor;
        }
        
        public function get containerMgr() : IContainerManager
        {
            return this._containerMgr;
        }
        
        public function get textMgr() : ITextManager
        {
            return this._textMgr;
        }
        
        public function get contextMenuMgr() : IContextMenuManager
        {
            return this._contextMenuMgr;
        }
        
        public function get popoverMgr() : IPopoverManager
        {
            return this._popoverMgr;
        }
        
        public function get colorSchemeMgr() : IColorSchemeManager
        {
            return this._colorSchemeMgr;
        }
        
        public function get voiceChatMgr() : IVoiceChatManager
        {
            return this._voiceChatMgr;
        }
        
        public function get gameInputMgr() : IGameInputManager
        {
            return this._gameInputMgr;
        }
        
        public function get eventLogManager() : IEventLogManager
        {
            return this.eventLogManager;
        }
        
        public function get loaderMgr() : ILoaderManager
        {
            return this._loaderMgr;
        }
        
        public function get cacheMgr() : ICacheManager
        {
            return this._cacheMgr;
        }
        
        public function get utils() : IUtils
        {
            return this._utils;
        }
        
        public function get tweenMgr() : ITweenManager
        {
            return this._tweenMgr;
        }
        
        public function get browserBgClass() : Class
        {
            return null;
        }
        
        public function get altBrowserBgClass() : Class
        {
            return null;
        }
        
        public function get tutorialMgr() : ITutorialManager
        {
            return null;
        }
        
        public function get atlasMgr() : IAtlasManager
        {
            return null;
        }
    }
}
