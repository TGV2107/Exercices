package Objets.Sylvain;

import java.util.HashMap;
import java.util.Map;

//Vive les tulipes
public class tulipe {
    private boolean isNoob;

    private Map<String, Integer> noob = new HashMap<>();

    public tulipe(boolean isNoob, Map<String, Integer> noob){
        this.isNoob = isNoob;
        this.noob = noob;
    }

    public boolean isNoob(){
        return this.isNoob;
    }

    public Map<String, Integer> getNoob(){
        return this.noob;
    }
}
