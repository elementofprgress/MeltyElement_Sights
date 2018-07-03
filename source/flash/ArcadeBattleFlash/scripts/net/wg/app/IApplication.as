package net.wg.app
{
    import net.wg.infrastructure.base.meta.IApplicationMeta;
    import flash.display.Stage;
    import flash.display.DisplayObjectContainer;
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
    import net.wg.infrastructure.managers.IEventLogManager;
    import net.wg.infrastructure.managers.ILoaderManager;
    import net.wg.infrastructure.managers.ICacheManager;
    import net.wg.infrastructure.managers.ITutorialManager;
    import net.wg.infrastructure.managers.IAtlasManager;
    import net.wg.utils.IUtils;
    import net.wg.utils.ITweenManager;
    import net.wg.infrastructure.interfaces.IManagedContainer;
    
    public interface IApplication extends IApplicationMeta
    {
         
        function get appWidth() : Number;
        
        function get appHeight() : Number;
        
        function get appScale() : Number;
        
        function get stage() : Stage;
        
        function get systemMessages() : DisplayObjectContainer;
        
        function get globalVarsMgr() : IGlobalVarsManager;
        
        function get soundMgr() : ISoundManager;
        
        function get toolTipMgr() : ITooltipMgr;
        
        function get waiting() : IWaitingView;
        
        function get environment() : IEnvironmentManager;
        
        function get cursor() : ICursor;
        
        function get containerMgr() : IContainerManager;
        
        function get textMgr() : ITextManager;
        
        function get contextMenuMgr() : IContextMenuManager;
        
        function get popoverMgr() : IPopoverManager;
        
        function get colorSchemeMgr() : IColorSchemeManager;
        
        function get voiceChatMgr() : IVoiceChatManager;
        
        function get gameInputMgr() : IGameInputManager;
        
        function get eventLogManager() : IEventLogManager;
        
        function get loaderMgr() : ILoaderManager;
        
        function get cacheMgr() : ICacheManager;
        
        function get tutorialMgr() : ITutorialManager;
        
        function get atlasMgr() : IAtlasManager;
        
        function get utils() : IUtils;
        
        function get tweenMgr() : ITweenManager;
        
        function get browserBgClass() : Class;
        
        function get altBrowserBgClass() : Class;
        
        function getManagedContainer(param1:String) : IManagedContainer;
    }
}
