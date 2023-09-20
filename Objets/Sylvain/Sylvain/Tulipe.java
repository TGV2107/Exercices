package Sylvain;

import java.util.HashMap;
import java.util.Map;

//Vive les tulipes
public class Tulipe {
    private String name;
    private boolean isNoob;
    private Map<String, Integer> noob = new HashMap<>();

    public Tulipe(String name, boolean isNoob, Map<String, Integer> noob){
        this.name = name;
        this.isNoob = isNoob;
        this.noob = noob;
    }

    public String getName(){
        return this.name;
    }

    public void setName(String name){
        this.name = name;
    }

    public boolean isNoob(){
        return this.isNoob;
    }

    public Map<String, Integer> getNoob(){
        return this.noob;
    }
}
