package net.wg.infrastructure.base.meta
{
    import flash.events.IEventDispatcher;
    import net.wg.infrastructure.interfaces.IStrCaseProperties;
    import net.wg.infrastructure.interfaces.IImageUrlProperties;
    
    public interface IUtilsManagerMeta extends IEventDispatcher
    {
         
        function getNationNamesS() : Array;
        
        function getNationIndicesS() : Object;
        
        function getGUINationsS() : Array;
        
        function changeStringCasingS(param1:String, param2:Boolean, param3:IStrCaseProperties) : String;
        
        function getAbsoluteUrlS(param1:String) : String;
        
        function getHtmlIconTextS(param1:IImageUrlProperties) : String;
        
        function getFirstDayOfWeekS() : int;
        
        function getWeekDayNamesS(param1:Boolean = true, param2:Boolean = false, param3:Boolean = false) : Array;
        
        function getMonthsNamesS(param1:Boolean = true, param2:Boolean = false, param3:Boolean = false) : Array;
        
        function intToStringWithPrefixPaternS(param1:int, param2:int, param3:String) : String;
        
        function isTwelveHoursFormatS() : Boolean;
        
        function as_setImageCacheSettings(param1:int, param2:int) : void;
    }
}
