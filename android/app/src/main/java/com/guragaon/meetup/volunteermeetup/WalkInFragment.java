package com.guragaon.meetup.volunteermeetup;


import android.os.Bundle;
import android.app.Fragment;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.guragaon.meetup.volunteermeetup.Utils.Constants;

import java.util.HashMap;
import java.util.Map;


/**
 * A simple {@link Fragment} subclass.
 */
public class WalkInFragment extends Fragment
{

    RecyclerView eventsList;
    LinearLayoutManager linearLayoutManager;

    public WalkInFragment()
    {

    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view= inflater.inflate(R.layout.fragment_walk_in, container, false);
        eventsList=(RecyclerView) view.findViewById(R.id.eventList);
        linearLayoutManager=new LinearLayoutManager(getActivity(),LinearLayoutManager.VERTICAL,false);
        eventsList.setLayoutManager(linearLayoutManager);

        StringRequest request = new StringRequest(Request.Method.POST, Constants.EVENTSLISTPAGEURL,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {

                    }
                }) {
            @Override
            protected Map<String, String> getParams() throws AuthFailureError {
                Map<String,String> map=new HashMap<>();
                map.put("","");
                return map;
            }
        };
        VolleyRequestQueue.getInstance(getActivity()).addToRequestQueue(request);

        return view;
    }

}
