package net.wg.mock.utils
{
    import net.wg.utils.IIcons;
    
    public class MockIcons implements IIcons
    {
         
        public function MockIcons()
        {
            super();
        }
        
        public function getIcon16StrPath(iconId:String) : String
        {
            return "";
        }
    }
}
