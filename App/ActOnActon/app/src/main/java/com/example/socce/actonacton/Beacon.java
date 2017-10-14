package com.example.socce.actonacton;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

/**
 * Tries to connect to beacons
 */

class Beacon extends WaitingActivity {

    public boolean searcher;
    public BeaconItem nearestBeacon;

    public Beacon() {
        this.searcher = true;
        this.nearestBeacon = null;
    }

    public void searchForBeacon(){
        while(searcher){
            // Search for beacon
            if(beaconDetected()){
                int beaconID = nearestBeaconID();
                if(isOurBeacon(beaconID)){

                }
            }
        }
    }

    public boolean beaconDetected(){
        // TODO
        return false;
    }

    public int nearestBeaconID(){
        // TODO
        return 0;
    }

    public boolean isOurBeacon(int id){
        return !(id<0 || id > 99999999);
    }

    public JSONArray getStoreDeals(){
        //connect to server to http get
        return null;
    }

    public StoreDealsObject[] returnStoreDeals(JSONArray deals) throws JSONException {
        int size = deals.length();
        StoreDealsObject[] ourDeals = new StoreDealsObject[size];
        for(int i=0; i<size; i++){
            JSONObject deal;
            try {
                deal = deals.getJSONObject(i);
            }
            catch (Exception e){
                throw new JSONException("Failure to parse object");
            }
            ourDeals[i] = Parsing.getStoreDeal(deal);
        }
        return ourDeals;
    }

    public JSONObject getDirection(){
        // Connect to aws via http get/post,
        return null;
    }

    public DirectionsObject returnDirection(JSONObject directionjson){
        // parse and return data
        return null;
    }

}
