package com.example.fbcircle;

import android.app.Activity;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;

import com.google.zxing.Result;

import me.dm7.barcodescanner.zxing.ZXingScannerView;

/**<p>
 * Created by angads25 on 28-08-2016.
 * </p>
 */

public class ScannerFragment extends Fragment implements ZXingScannerView.ResultHandler{
    private ZXingScannerView mScannerView;

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View V=inflater.inflate(R.layout.fragment_scanner,container,false);
        mScannerView =(ZXingScannerView)V.findViewById(R.id.qr_scanner);
        mScannerView.setAutoFocus(true);
        return V;
    }
    @Override
    public void onResume() {
        super.onResume();
        mScannerView.setResultHandler(this);
        mScannerView.startCamera();
    }

    @Override
    public void onPause() {
        super.onPause();
        mScannerView.stopCamera();
    }

    @Override
    public void handleResult(Result rawResult)
    {   String id = rawResult.getText();
        Log.e("TAG",id);
        Toast.makeText(getContext(),"Code Scanned",Toast.LENGTH_SHORT).show();
        Thread T1=new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    Thread.sleep(2000);
                }
                catch (InterruptedException e) {
                    e.printStackTrace();
                }
                finally
                {   ((Activity)getContext()).runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        mScannerView.resumeCameraPreview(ScannerFragment.this);
                    }
                });
                }
            }
        });
        T1.start();
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        mScannerView.stopCameraPreview();
    }
}
