package Perceptron_Multi_Classe;

import java.io.IOException;
import java.io.PrintWriter;

import mnisttools.MnistReader;

public class Graphe2 {
	/* Les donnees */
	public static String path="/home/tp-home010/tnaitla/Bureau/";
	public static String labelDB=path+"train-labels-idx1-ubyte";
	public static String imageDB=path+"train-images-idx3-ubyte";
 
	/* Parametres */
	// les N premiers exemples pour l'apprentissage
	public static final int N =1000; 
	// les T derniers exemples  pour l'evaluation
	public static final int T = 500; 
	// le nombre de classes
	public static final int K= 10 ; 
	// Nombre d'epoque max
	public final static int EPOCHMAX=40;
	// Classe positive (le reste sera considere comme des ex. negatifs):
	public static int  classe = 5 ;
	
 
 
 
	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		System.err.println("# Load the database !");
		/* Lecteur d'image */ 
		MnistReader db = new MnistReader(labelDB, imageDB);
		/* Taille des images et donc de l'espace de representation */
		final int SIZEW = ImageConverter.image2VecteurReel_withB(db.getImage(1)).length;
 
         //////////////////////////
		// Creation des donnees //
	   //////////////////////////
		
	//	System.err.println("# Build train for "+ classe);
		double[][] trainData = new double[N][SIZEW];
		double[][]VecRefs=new double[N][K];
		int cptPos=0;
		int cpt=0;
		
		 ///////////////////////////////
		/// Donnees d'apprentissage ///
	   ///////////////////////////////
		 
		for (int i = 1; i <= N ; i++) {
			cpt++;
			trainData[i-1]=ImageConverter.image2VecteurReel_withB(db.getImage(i));
			int label = db.getLabel(i);
			//////////////////////////////////////////////////////////
		   ////initialisation du tableau des etiquettes de données///
		  //////////////////////////////////////////////////////////
			for (int j = 0 ; j < VecRefs[i-1].length;j++){
				if(j==label){
				  VecRefs[i-1][j]=1;
				}else{
				VecRefs[i-1][j]=0;
				}
			}
		}	
 
		//System.err.println("Train set with "+cptPos*100.0/cpt+ " % positives /"+cpt);
         ///////////////////////////
		////* Donnees de test *////
	   ///////////////////////////
		System.err.println("# Build test for "+ classe);
		cptPos=0;
		cpt=0;
		final int TOTAL = db.getTotalImages();
		if (N+T >= TOTAL){
			//System.out.println("N+T > Total");
			throw new RuntimeException();
		}
		double[][] testData = new double[T][SIZEW];
		double[][] VecRefstest = new double[T][K];
		for (int i = 0; i < T; i++) {
			cpt++;
			testData[i]=ImageConverter.image2VecteurReel_withB(db.getImage(TOTAL-i));
			int label = db.getLabel(TOTAL-i);
                ///////////////////////////////////////////////////////////////////
               ////initialisation du tableau des etiquettes de données de test ///
              ///////////////////////////////////////////////////////////////////
			for (int j = 0 ; j < VecRefstest[i].length;j++){
			if(j==label){
			  VecRefstest[i][j]=1;
			}else{
			VecRefstest[i][j]=0;
			}
		}
			
		}
		System.err.println("Test set with "+cptPos*100.0/cpt+ " % positives /"+cpt);
		 
		 /////////////////////////////////////////////////////////////////////////////////////
		/////////// on récupere les poids de chaque perceptro en appellant la  //////////////
	   ///////////         la fonction Perceptron_multi                       //////////////
	  /////////////////////////////////////////////////////////////////////////////////////
		 int [] Graphetest = new int [101]; 
		 int [] Graphetrain = new int [101];
		for (int nbepoque = 1; nbepoque <= 100 ;nbepoque++ ){
		double[][]w =  Algorithme_Code.Preceptron_Multi (trainData , VecRefs ,0.01,nbepoque) ;    
	     
	     
	  ////////////////////////////////////////////////////////////////////////////////////////
	 /////////////// on fait le test sur l'ensemble de test < testData >  ///////////////////
	///////////////    et afficher le nombre de donnée mal Classées       //////////////////
   ////////////////////////////////////////////////////////////////////////////////////////  
	int nberrtest = 0 ;
	int nberrtrain = 0 ; 
	double scal = 0;
	for (int i = 0 ; i < testData.length;i++){
		/// cherche la classe de i-emme donnée 
		int Classe = Algorithme_Code.indiceMax(VecRefstest[i]);
		int classePerceptron =  Algorithme_Code.indiceMax(Algorithme_Code.tableau_proba(testData[i],Algorithme_Code.sommeProba (testData[i],w),w));
	    scal = Algorithme_Code.Produit_Scal(w[Classe], testData[i]);
		if(Classe != classePerceptron ){
			nberrtest++;
			//System.out.println("la donnée  "+i+" est mal classé et elle represente le chiffre "+Classe + " et il est consideré par le perceptron comme in "+classePerceptron );
		}
	}
	for (int i = 0 ; i < trainData.length;i++){
		/// cherche la classe de i-emme donnée 
		int Classe = Algorithme_Code.indiceMax(VecRefs[i]);
		int classePerceptron =  Algorithme_Code.indiceMax(Algorithme_Code.tableau_proba(trainData[i],Algorithme_Code.sommeProba (trainData[i],w),w));
	    scal = Algorithme_Code.Produit_Scal(w[Classe], trainData[i]);
		if(Classe != classePerceptron ){
			nberrtrain++;
			//System.out.println("la donnée  "+i+" est mal classé et elle represente le chiffre "+Classe + " et il est consideré par le perceptron comme in "+classePerceptron );
		}
	}
	   Graphetrain[nbepoque-1]=nberrtrain;
       Graphetest[nbepoque-1]=nberrtest;
       System.out.println(nbepoque);
	  // System.out.println("le nombre de données mal Classé est "+nberr+" avec un pourcentage de "+(float)nberr*100/T+"%");
	
		}
		PrintWriter writer = new PrintWriter("datatest.txt", "UTF-8");
		PrintWriter writer1 = new PrintWriter("datatrain.txt", "UTF-8");
		for(int k =0 ; k < 100 ; k++){
		int g =0 ;
		writer.println(k+" "+Graphetest[k]);
		writer1.println(k+" "+Graphetrain[k]);
		//writer.println("La deuxième ligne");
		
		}
		writer.close();
		writer1.close();
		
	}

}
