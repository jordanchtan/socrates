package com.example.socce.actonacton;

/**
 * Beacon object holding details about beacon
 * Beacon opcode is 2-bits for store no, 3 bits on aisle no, 3 bits on part of aisle
 * Opcode for storefront is if bits 2-7 are all 0s
 */

public class BeaconItem {

    private final int beaconID;
    private final int MAX_OPCODE_SIZE = 99999999;
    private final int MIN_OPCODE_SIZE = 0;

    public BeaconItem(int beaconID) {
        if(beaconID>MAX_OPCODE_SIZE || beaconID < MIN_OPCODE_SIZE){
            throw new IndexOutOfBoundsException("Beacon ID is Faulty!");
        }
        this.beaconID = beaconID;
    }

    public int getBeaconID(){
        return beaconID;
    }

    public boolean isStoreFront(){
        return ((beaconID % 1000000)==0);
    }

    public int getStoreNo(){
        return (beaconID/1000000);
    }

    public int getAisle(){
        return ((beaconID/1000)%1000);
    }

    public int getPartOfAisle(){
        return (beaconID%1000);
    }
}
