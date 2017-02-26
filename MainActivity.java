package dev.edmt.todolist;

import android.content.Context;
import android.content.DialogInterface;
import android.content.res.Resources;
import android.graphics.PorterDuff;
import android.graphics.drawable.Drawable;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.Spinner;
import android.widget.TextView;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.*;

public class MainActivity extends AppCompatActivity {

    DbHelper dbHelper;
    ArrayAdapter<String> mAdapter;
    ListView lstTask;
    private String[] arraySpinner;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        dbHelper = new DbHelper(this);

        lstTask = (ListView)findViewById(R.id.lstTask);

        loadTaskList();
    }

    private void loadTaskList() {
        ArrayList<String> taskList = dbHelper.getTaskList();
        if(mAdapter==null){
            mAdapter = new ArrayAdapter<>(this,R.layout.row,R.id.task_title,taskList);
            lstTask.setAdapter(mAdapter);
        }
        else{
            mAdapter.clear();
            mAdapter.addAll(taskList);
            mAdapter.notifyDataSetChanged();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.menu,menu);

        //Change menu icon color
        Drawable icon = menu.getItem(0).getIcon();
        icon.mutate();
        icon.setColorFilter(getResources().getColor(android.R.color.white), PorterDuff.Mode.SRC_IN);

        return super.onCreateOptionsMenu(menu);
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        this.arraySpinner = new String[] {"Water", "Food", "Medical"};
        final Spinner spinner = new Spinner(this);
        ArrayAdapter<String> adapter = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, arraySpinner);
        spinner.setAdapter(adapter);
        final String co1 = ": 18.550, -72.300";
        final String co2 = ": 17.135, -72.666";
        final String co3 = ": 16.937, -76.124";
        final String co4 = ": 19.234, -67.234";
        final String co5 = ": 17.124, -70.986";
        final EditText editText = (EditText) findViewById(R.id.Id);
        FirebaseDatabase database = FirebaseDatabase.getInstance();
        final DatabaseReference myRef = database.getReference("dispatch1");
        final DatabaseReference myRef2 = database.getReference("dispatch2");
        final DatabaseReference myRef3 = database.getReference("dispatch3");
        final DatabaseReference myRef4 = database.getReference("dispatch4");
        final DatabaseReference myRef5 = database.getReference("dispatch5");
        LinearLayout layout = new LinearLayout(this);
        layout.setOrientation(LinearLayout.VERTICAL);
        layout.addView(spinner);
        final EditText titleBox = new EditText(this);
        titleBox.setHint("People");
        layout.addView(titleBox);
        switch (item.getItemId()){
            case R.id.action_add_task:
                AlertDialog dialog = new AlertDialog.Builder(this)
                        .setTitle("Add resource claim: ")
                        .setMessage("You are at: 18.550996, -72.300748")
                        .setView(layout)
                        .setPositiveButton("Add", new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                switch ((int) Math.round(Math.random()*5)){
                                    case 0:
                                        dbHelper.insertNewTask(String.valueOf(spinner.getSelectedItem().toString()+" for "+titleBox.getText().toString() + co1));
                                        loadTaskList();
                                        myRef.setValue(spinner.getSelectedItem().toString()+ " " +titleBox.getText().toString() + co1);
                                        break;
                                    case 1:
                                        dbHelper.insertNewTask(String.valueOf(spinner.getSelectedItem().toString()+" for "+titleBox.getText().toString() + co2));
                                        loadTaskList();
                                        myRef2.setValue(spinner.getSelectedItem().toString()+ " " +titleBox.getText().toString() + co2);
                                        break;
                                    case 2:
                                        dbHelper.insertNewTask(String.valueOf(spinner.getSelectedItem().toString()+" for "+titleBox.getText().toString() + co3));
                                        loadTaskList();
                                        myRef3.setValue(spinner.getSelectedItem().toString()+ " " +titleBox.getText().toString() + co3);
                                        break;
                                    case 3:
                                        dbHelper.insertNewTask(String.valueOf(spinner.getSelectedItem().toString()+" for "+titleBox.getText().toString() + co4));
                                        loadTaskList();
                                        myRef4.setValue(spinner.getSelectedItem().toString()+ " " +titleBox.getText().toString() + co4);
                                        break;
                                    default:
                                        dbHelper.insertNewTask(String.valueOf((spinner.getSelectedItem().toString())+" for "+titleBox.getText().toString() + co5));
                                        loadTaskList();
                                        myRef5.setValue(spinner.getSelectedItem().toString() + " " +titleBox.getText().toString()+ co5);
                                        break;
                                }
                                //editText.setText(titleBox.getText().toString(), TextView.BufferType.EDITABLE);

                                /*myRef.setValue("Water,18.550996,-72.300748");
                                myRef2.setValue("Food,18.550996,-72.300748");
                                myRef3.setValue("Medicine,18.550996,-72.300748");
                                myRef4.setValue("Road Block,18.550996,-72.300748");
                                myRef5.setValue("Water,18.550996,-72.300748");
                                String task = String.valueOf(taskEditText.getText() + co);
                                dbHelper.insertNewTask(task);
                                loadTaskList();*/
                            }
                        })
                        .setNegativeButton("Cancel",null)
                        .create();
                dialog.show();
                return true;
        }
        return super.onOptionsItemSelected(item);
    }

    public void deleteTask(View view){
        View parent = (View)view.getParent();
        TextView taskTextView = (TextView)parent.findViewById(R.id.task_title);
        Log.e("String", (String) taskTextView.getText());
        String task = String.valueOf(taskTextView.getText());
        dbHelper.deleteTask(task);
        loadTaskList();
    }
}



                          /*switch (taskEditText.getText().toString()){
                                    case "water":
                                        keys.put("water");
                                        break;
                                    case "food":
                                        break;
                                    case "medicine":
                                        break;
                                    default:
                                        break;
                                }*/