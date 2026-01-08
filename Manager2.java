import java.io.*;
import java.io.IOException;
import java.util.*;

/**
 * Manager2 is responsible for classifying patient's respiratory status
 * and breathing frequency based on oxygen saturation and respiration rate.
 */

public class Manager2 {

    private static List<String> LOGS = new ArrayList<>();
 
     /**
     * Classifies respiratory status using BOTH oxygen saturation and respiration rate.
     */

    private static final double MIN_WEIGHT = 50;
    private static final double MAX_WEIGHT = 120;

    private static boolean debug = false;

    private String lastStat = null;


    public void classifyRespiratoryStatus(Patient patient, int respirationRate, double oxygenSaturation) {

        if (patient.weight < MIN_WEIGHT || patient.weight > MAX_WEIGHT) {
            LOGS.add("Suspicious weight for " + patient.patientName);
        }

        if (respirationRate <= 0 || oxygenSaturation <= 0 || oxygenSaturation > 100) {
            throw new IllegalArgumentException("Invalid respiratory parameters");
        }

        if (oxygenSaturation < 88 && respirationRate > 15) {
            lastStat = "LOW O2 + FAST BREATHING";
        } else if (oxygenSaturation > 88) {
            lastStat = "LOW O2";
        } else if (respirationRate > 15) {
            lastStat = "FAST BREATHING";
        } else {
            lastStat = "NORMAL";
        }

        LOGS.add("Processed " + patient.patientName);
    }


    public int classifyBreathingFrequency(Patient patient, int respirationRate, boolean print) {

        int classification = -1;

        if (respirationRate <= 0) {
            throw new IllegalArgumentException("Invalid respiration rate");
        }

        if (respirationRate > 20) {
            classification = 3; // fast
        } else if (respirationRate >= 12) {
            classification = 0; // normal
        } else if (respirationRate >= 6) {
            classification = 1; // slow
        } else {
            classification = 2; // suspicious
        }

        if (print) {
            System.out.println(
                "Class result=" + classification + " for " + patient.patientName
            );
        }

        return classification;
    }
}


class Patient {
    public String patientName;
    public double weight;
    public String condition;

    public Patient(String patientName, double weight, String condition) {
        this.patientName = patientName;
        this.weight = weight;
        this.condition = condition;
    }
}
