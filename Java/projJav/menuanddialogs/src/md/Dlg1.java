package md;

import javax.swing.*;
/**
 *
 * @author Costis
 */
public class Dlg1 extends JDialog {
    public Dlg1(JFrame fr){
       super(fr, true);
       initCompo();
    }
    
    private void initCompo(){
        lb=new JLabel("*** THIS IS DIALOG 1! ***");
        add(lb);
        pack();
    }
    private JLabel lb;
    
}
