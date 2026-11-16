package local.amap.voice;
import android.content.Context;
import android.os.Handler;
import android.os.Looper;
import android.util.Log;
import java.lang.reflect.Method;

/** Shift only the original cluster anchor. No location, camera centre or follow writes. */
public final class ClusterAnchor {
 private static boolean started;
 private static final Handler main=new Handler(Looper.getMainLooper());
 private static final float SHIFT_PIXELS=64f;
 private static Object call(Object o,String name,Object...args)throws Exception {
  for(Method m:o.getClass().getMethods())if(m.getName().equals(name)&&m.getParameterTypes().length==args.length)
   try{return m.invoke(o,args);}catch(IllegalArgumentException ignored){}
  throw new NoSuchMethodException(name);
 }
 private static Object singleton(Context c,String name)throws Exception {
  return Class.forName(name,false,c.getClassLoader()).getMethod("getInstance").invoke(null);
 }
 public static synchronized void start(Context context){
  if(started)return;started=true;final Context c=context.getApplicationContext();
  main.postDelayed(new Runnable(){public void run(){
   try{apply(c);}catch(Exception ignored){}
   main.postDelayed(this,1500);
  }},1500);
 }
 private static void apply(Context c)throws Exception {
  Object maps=singleton(c,"com.leapmotor.autonavi.core.autosdk.map.MapController");
  Object view=call(maps,"getMapView",3);if(view==null||((Number)call(view,"getEngineId")).intValue()!=5)return;
  Object layer=call(singleton(c,"com.leapmotor.autonavi.core.autosdk.layer.LayerController"),"getMapLayer",3);
  Object car=call(layer,"getCarControl");
  if(!Boolean.TRUE.equals(call(car,"getFollowMode"))||Boolean.TRUE.equals(call(car,"getPreviewMode")))return;
  Object projection=call(view,"getMapProjectionCenter");
  float x=((Number)projection.getClass().getField("percentX").get(projection)).floatValue();
  float y=((Number)projection.getClass().getField("percentY").get(projection)).floatValue();
  // Only consume an OEM anchor reset. Already shifted or custom anchors remain untouched.
  if(Math.abs(x-.5f)>.001f||!(Math.abs(y-2f/3f)<.001f||Math.abs(y-.70f)<.001f||Math.abs(y-.76f)<.001f))return;
  Object viewport=call(call(view,"getOperatorPosture"),"getViewSize");
  int height=((Number)viewport.getClass().getField("height").get(viewport)).intValue();
  if(height!=720)return;
  float target=y-SHIFT_PIXELS/height;
  call(view,"setMapProjectionCenter",x,target);
  Object after=call(view,"getMapProjectionCenter");
  org.json.JSONObject status=new org.json.JSONObject().put("time_ms",System.currentTimeMillis()).put("surface",3).put("engine",5).put("before_y",y).put("after_y",after.getClass().getField("percentY").get(after)).put("shift_px",64).put("follow",call(car,"getFollowMode")).put("preview",call(car,"getPreviewMode"));
  Object mainView=call(maps,"getMapView",1);if(mainView!=null){Object mp=call(mainView,"getMapProjectionCenter");status.put("main_projection_y",mp.getClass().getField("percentY").get(mp));}
  java.nio.file.Files.write(new java.io.File(c.getFilesDir(),"cluster-anchor-status.json").toPath(),status.toString(2).getBytes("UTF-8"));
  Log.i("UYClusterAnchor","surface=3 engine=5 before="+y+" after="+target+" shift_px=64");
 }
}
