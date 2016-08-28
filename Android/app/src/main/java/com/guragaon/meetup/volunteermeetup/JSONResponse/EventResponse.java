package com.guragaon.meetup.volunteermeetup.JSONResponse;

import android.util.Log;

import org.json.JSONException;
import org.json.JSONObject;

/**
 * Created by mrsinghania on 28/8/16.
 */
public class EventResponse {

    String selectedId;
    JSONObject param;
    String TAG=getClass().getName();

    public EventResponse(String selectedId) {
        this.selectedId=selectedId;
    }

    public JSONObject buildjson() {
        try {
            param = new JSONObject();
            param.put("selectedId",selectedId);
            Log.v(TAG, param.toString());
        }
        catch (JSONException e) {
            e.printStackTrace();
        }
        return param;
    }

    public boolean parsejson(String jsonResponse) {
        if (jsonResponse != null) {
            try {

                JSONObject jsonObjMain = new JSONObject(jsonResponse);

            } catch (JSONException e) {
                e.printStackTrace();
                return false;
            }
        }
        return false;
    }
}
