package com.guragaon.meetup.volunteermeetup;

import android.content.Context;
import android.content.SharedPreferences;

import java.security.Key;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by shakshi on 09-07-2016.
 */
public class PreferenceManager {

    private static SharedPreferences sp;

    public enum Keys{

        UNSUCCESSFULL_ATTEMPTS

    }

    public static SharedPreferences.Editor getPreferenceEditor(Context context){
        sp = context.getSharedPreferences("volunteer", Context.MODE_PRIVATE);
        return sp.edit();
    }

    public static SharedPreferences getPreferences(Context context){
        sp = context.getSharedPreferences("volunteer", Context.MODE_PRIVATE);
        return sp;
    }

    public Set<String> getUnsuccessfullIds(Context context){
        Set<String> output=null;

        sp=context.getSharedPreferences("volunteer", Context.MODE_PRIVATE);
        sp.getStringSet(Keys.UNSUCCESSFULL_ATTEMPTS.toString(),null);

        return output;
    }

    public Set<String> addUnsuccessfullIds(Context context){
        Set<String> output=new HashSet<>();

        sp=context.getSharedPreferences("volunteer", Context.MODE_PRIVATE);
        SharedPreferences.Editor editor=sp.edit();
        Set<String> previousIds=sp.getStringSet(Keys.UNSUCCESSFULL_ATTEMPTS.toString(),null);

        for(String id:previousIds){
            output.add(id);
        }

        editor.remove(Keys.UNSUCCESSFULL_ATTEMPTS.toString());
        editor.apply();

        editor.putStringSet(Keys.UNSUCCESSFULL_ATTEMPTS.toString(),output);
        editor.apply();


        return output;
    }

    public Set<String> clearUnsuccessfullIds(Context context){
        Set<String> output=null;

        sp=context.getSharedPreferences("volunteer", Context.MODE_PRIVATE);
        sp.getStringSet(Keys.UNSUCCESSFULL_ATTEMPTS.toString(),null);

        return output;
    }


}
