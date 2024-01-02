package md;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

/**
 *
 * @author Costis
 */
public class MenuClass extends JFrame {
    public MenuClass(){
        initCompo();
        d1=new Dlg1(this);
        d2=new Dlg2(this);
    }
    
    private void initCompo(){
        mb=new JMenuBar();
        mnu=new JMenu("Dialogs");
        dlg1=new JMenuItem("Dialog 1");
        dlg1.addActionListener(new ActionListener(){
            @Override 
            public void actionPerformed(ActionEvent e) {
                d1.setVisible(true);
            }
        });
        dlg2=new JMenuItem("Dialog 2");
        dlg2.addActionListener(new ActionListener(){
            @Override 
            public void actionPerformed(ActionEvent e) {
                d2.setVisible(true);
            }
        });        
        mb.add(mnu);
        mnu.add(dlg1);
        mnu.add(dlg2);
        setJMenuBar(mb);
        
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        pack();
    }
    
    public static void main(String[] args) {
        new MenuClass().setVisible(true);
    }
    private JMenuBar mb;
    private JMenu mnu;
    private JMenuItem dlg1, dlg2;
    private Dlg1 d1;
    private Dlg2 d2;
}
