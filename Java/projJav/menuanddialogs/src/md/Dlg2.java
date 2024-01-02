package md;

import javax.swing.*;
/**
 *
 * @author Costis
 */
public class Dlg2 extends JDialog {
    public Dlg2(JFrame fr){
       super(fr, true);
       initCompo();
    }
    
    private void initCompo(){
        lb=new JLabel("*** THIS IS DIALOG 2 !!! ***");
        add(lb);
        pack();
    }
    private JLabel lb;
    
}
